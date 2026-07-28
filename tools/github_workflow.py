#!/usr/bin/env python3
"""Small deterministic GitHub Issue/Project/release helper.

The helper delegates authentication to the user's non-interactive ``gh``
installation. It never accepts or prints token values. Project field values
are resolved by field name at runtime so the helper remains portable across
Projects while still failing clearly when the configured schema is wrong.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from typing import Any


SECRET_PATTERNS = (
    re.compile(r"gh[pousr]_[A-Za-z0-9_\-]+"),
    re.compile(r"github_pat_[A-Za-z0-9_\-]+"),
    re.compile(r"(?i)(token|password|secret)=\S+"),
)


def scrub(value: str) -> str:
    for pattern in SECRET_PATTERNS:
        value = pattern.sub(lambda m: m.group(0).split("=")[0] + "=<redacted>" if "=" in m.group(0) else "<redacted>", value)
    return value


def run_gh(*args: str, input_data: str | None = None) -> str:
    proc = subprocess.run(
        ["gh", *args],
        input=input_data,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if proc.returncode:
        message = scrub((proc.stderr or proc.stdout).strip())
        raise RuntimeError(f"gh {' '.join(args[:2])} failed: {message}")
    return proc.stdout


def graphql(query: str, variables: dict[str, Any]) -> dict[str, Any]:
    raw = run_gh(
        "api",
        "graphql",
        "--input",
        "-",
        input_data=json.dumps({"query": query, "variables": variables}),
    )
    payload = json.loads(raw)
    if payload.get("errors"):
        raise RuntimeError(scrub(json.dumps(payload["errors"], ensure_ascii=False)))
    return payload.get("data", {})


def issue_node(repo: str, number: int) -> str:
    return run_gh("api", f"repos/{repo}/issues/{number}", "--jq", ".node_id").strip()


def issue_details(repo: str, number: int) -> dict[str, Any]:
    return json.loads(run_gh("api", f"repos/{repo}/issues/{number}"))


def project_fields(project_id: str) -> dict[str, Any]:
    query = """
    query($id:ID!) {
      node(id:$id) {
        ... on ProjectV2 {
          id
          title
          number
          fields(first:100) { nodes {
            __typename
            ... on ProjectV2Field { id name dataType }
            ... on ProjectV2SingleSelectField {
              id name dataType options { id name }
            }
          } }
          views(first:100) { nodes { id name number layout } }
        }
      }
    }
    """
    data = graphql(query, {"id": project_id})
    project = data.get("node")
    if not project:
        raise RuntimeError(f"Project not found: {project_id}")
    return project


def project_item(project_id: str, content_id: str) -> dict[str, Any]:
    query = """
    mutation($projectId:ID!, $contentId:ID!) {
      addProjectV2ItemById(input:{projectId:$projectId, contentId:$contentId}) {
        item { id content { ... on Issue { number } ... on PullRequest { number } } }
      }
    }
    """
    data = graphql(query, {"projectId": project_id, "contentId": content_id})
    return data["addProjectV2ItemById"]["item"]


def set_field(project_id: str, item_id: str, field_id: str, value: dict[str, Any]) -> dict[str, Any]:
    query = """
    mutation($projectId:ID!, $itemId:ID!, $fieldId:ID!, $value:ProjectV2FieldValue!) {
      updateProjectV2ItemFieldValue(input:{projectId:$projectId,itemId:$itemId,fieldId:$fieldId,value:$value}) {
        projectV2Item { id }
      }
    }
    """
    data = graphql(query, {"projectId": project_id, "itemId": item_id, "fieldId": field_id, "value": value})
    return data["updateProjectV2ItemFieldValue"]["projectV2Item"]


def cmd_issue_project(args: argparse.Namespace) -> dict[str, Any]:
    content_id = issue_node(args.repo, args.issue)
    item = project_item(args.project_id, content_id)
    result: dict[str, Any] = {"repository": args.repo, "issue": args.issue, "item_id": item["id"]}
    if args.field_id and args.option_id:
        result["field"] = set_field(args.project_id, item["id"], args.field_id, {"singleSelectOptionId": args.option_id})
    elif args.field_id and args.text is not None:
        result["field"] = set_field(args.project_id, item["id"], args.field_id, {"text": args.text})
    return result


def find_exact_issue(repo: str, title: str) -> dict[str, Any] | None:
    escaped_title = title.replace('"', '\\"')
    query = f'repo:{repo} is:issue in:title "{escaped_title}"'
    payload = json.loads(
        run_gh(
            "api",
            "search/issues",
            "-f",
            f"q={query}",
            "-f",
            "per_page=100",
        )
    )
    matches = [item for item in payload.get("items", []) if item.get("title") == title]
    if not matches:
        return None
    return sorted(matches, key=lambda item: item.get("number", 0))[0]


def create_issue(repo: str, title: str, body: str, labels: list[str]) -> dict[str, Any]:
    payload: dict[str, Any] = {"title": title, "body": body}
    if labels:
        payload["labels"] = labels
    return json.loads(
        run_gh(
            "api",
            f"repos/{repo}/issues",
            "--method",
            "POST",
            "--input",
            "-",
            input_data=json.dumps(payload),
        )
    )


PROJECT_FIELD_ARGS = {
    "Status": "status",
    "Type": "type",
    "Priority": "priority",
    "Owner": "owner",
    "Scope": "scope",
    "Evidence": "evidence",
    "Module": "module",
}


def cmd_project_fields(args: argparse.Namespace) -> dict[str, Any]:
    project = project_fields(args.project_id)
    return {
        "project_id": project["id"],
        "title": project.get("title"),
        "number": project.get("number"),
        "fields": project.get("fields", {}).get("nodes", []),
        "views": project.get("views", {}).get("nodes", []),
    }


def cmd_issue_create(args: argparse.Namespace) -> dict[str, Any]:
    existing = find_exact_issue(args.repo, args.title)
    if existing:
        issue = existing
        created = False
        number = int(issue["number"])
        if not issue.get("node_id"):
            issue = issue_details(args.repo, number)
    else:
        issue = create_issue(args.repo, args.title, args.body, args.label)
        created = True
        number = int(issue["number"])

    content_id = issue.get("node_id") or issue_node(args.repo, number)
    item = project_item(args.project_id, content_id)
    project = project_fields(args.project_id)
    fields = {field["name"]: field for field in project["fields"]["nodes"]}
    applied: dict[str, Any] = {}
    for field_name, argument_name in PROJECT_FIELD_ARGS.items():
        value = getattr(args, argument_name)
        if value is None:
            continue
        field = fields.get(field_name)
        if not field:
            raise RuntimeError(f"Project field not found: {field_name}")
        if field.get("dataType") == "SINGLE_SELECT":
            options = {option["name"]: option["id"] for option in field.get("options", [])}
            option_id = options.get(value)
            if not option_id:
                raise RuntimeError(f"Project option not found: {field_name}={value}")
            set_field(args.project_id, item["id"], field["id"], {"singleSelectOptionId": option_id})
        elif field.get("dataType") == "TEXT":
            set_field(args.project_id, item["id"], field["id"], {"text": value})
        else:
            raise RuntimeError(f"Unsupported Project field type: {field_name}={field.get('dataType')}")
        applied[field_name] = value

    return {
        "ok": True,
        "repository": args.repo,
        "issue": number,
        "issue_url": issue.get("html_url"),
        "created": created,
        "reused_existing_title": not created,
        "project_id": args.project_id,
        "project_item_id": item["id"],
        "fields": applied,
    }


def cmd_release_check(args: argparse.Namespace) -> dict[str, Any]:
    release = json.loads(run_gh("api", f"repos/{args.repo}/releases/tags/{args.tag}"))
    result = {
        "repository": args.repo,
        "tag": args.tag,
        "release_url": release.get("html_url"),
        "draft": release.get("draft"),
        "prerelease": release.get("prerelease"),
        "stable": not release.get("draft") and not release.get("prerelease"),
    }
    if not result["stable"]:
        raise RuntimeError(json.dumps(result))
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("issue-project", help="Add an existing Issue and set one Project field")
    add.add_argument("--repo", required=True)
    add.add_argument("--issue", required=True, type=int)
    add.add_argument("--project-id", required=True)
    add.add_argument("--field-id")
    add.add_argument("--option-id")
    add.add_argument("--text")
    add.set_defaults(handler=cmd_issue_project)
    fields = sub.add_parser("project-fields", help="Read Project fields, options, and views")
    fields.add_argument("--project-id", required=True)
    fields.set_defaults(handler=cmd_project_fields)
    create = sub.add_parser("issue-create", help="Create or reuse an Issue and configure its Project fields")
    create.add_argument("--repo", required=True)
    create.add_argument("--title", required=True)
    create.add_argument("--body", default="")
    create.add_argument("--label", action="append", default=[])
    create.add_argument("--project-id", required=True)
    create.add_argument("--status", default="Backlog")
    create.add_argument("--type", required=True)
    create.add_argument("--priority")
    create.add_argument("--owner", required=True)
    create.add_argument("--scope", required=True)
    create.add_argument("--evidence", default="Missing")
    create.add_argument("--module")
    create.set_defaults(handler=cmd_issue_create)
    release = sub.add_parser("release-check", help="Verify a normal GitHub release")
    release.add_argument("--repo", required=True)
    release.add_argument("--tag", required=True)
    release.set_defaults(handler=cmd_release_check)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        print(json.dumps(args.handler(args), ensure_ascii=False, sort_keys=True))
    except (RuntimeError, json.JSONDecodeError, KeyError) as exc:
        print(json.dumps({"ok": False, "error": scrub(str(exc))}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

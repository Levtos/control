#!/usr/bin/env python3
"""Small deterministic GitHub Issue/Project/release helper.

The helper delegates authentication to the user's non-interactive `gh`
installation. It never accepts or prints token values.
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
    raw = run_gh("api", "graphql", "-f", f"query={query}", "-f", f"variables={json.dumps(variables)}")
    payload = json.loads(raw)
    if payload.get("errors"):
        raise RuntimeError(scrub(json.dumps(payload["errors"], ensure_ascii=False)))
    return payload.get("data", {})


def issue_node(repo: str, number: int) -> str:
    return run_gh("api", f"repos/{repo}/issues/{number}", "--jq", ".node_id").strip()


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

import importlib.util
import pathlib
import unittest
from unittest import mock


MODULE = pathlib.Path(__file__).parents[1] / "tools" / "github_workflow.py"
SPEC = importlib.util.spec_from_file_location("github_workflow", MODULE)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


class HelperTests(unittest.TestCase):
    def test_scrub_github_token(self):
        self.assertNotIn("github_pat_", MOD.scrub("token=github_pat_secret"))

    def test_parser_has_commands(self):
        parser = MOD.build_parser()
        self.assertEqual(parser.parse_args(["release-check", "--repo", "Levtos/control", "--tag", "v1.0.0"]).repo, "Levtos/control")

    def test_issue_create_parser_exposes_project_fields(self):
        parser = MOD.build_parser()
        args = parser.parse_args([
            "issue-create",
            "--repo", "Levtos/control",
            "--title", "Example",
            "--project-id", "PVT_example",
            "--type", "Idea",
            "--owner", "Codex",
            "--scope", "Platform",
        ])
        self.assertEqual(args.status, "Backlog")
        self.assertEqual(args.evidence, "Missing")
        self.assertIsNone(args.priority)
        self.assertIsNone(args.module)

    def test_graphql_uses_structured_input_without_token_arguments(self):
        with mock.patch.object(MOD, "run_gh", return_value='{"data": {}}') as run:
            MOD.graphql("query($id:ID!){node(id:$id){id}}", {"id": "PVT_example"})
        args, kwargs = run.call_args
        self.assertEqual(args[:4], ("api", "graphql", "--input", "-"))
        self.assertIn('"variables"', kwargs["input_data"])
        self.assertNotIn("token", kwargs["input_data"].lower())


if __name__ == "__main__":
    unittest.main()

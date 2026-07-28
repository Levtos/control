import importlib.util
import pathlib
import unittest


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


if __name__ == "__main__":
    unittest.main()

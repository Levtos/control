# GitHub workflow

## Standard flow

1. Create or reuse a GitHub Issue.
2. Add it to the `Platform Workflow` Project and set known fields.
3. Read the Issue, comments, applicable Lastenheft, and repository rules.
4. Run the capability preflight.
5. Work in a clean isolated branch.
6. Run repository-local tests.
7. Open a pull request and inspect checks.
8. Merge server-side and verify the merge SHA.
9. For HACS work, create a stable patch tag and let the release Action create
   the normal release.
10. Verify HACS visibility. Leave the Issue at Testing until Benni's live
    gate.

Repository-local tests and central release automation are separate layers.
Do not create a test, runner, or CI gate that is not required by the Issue.

## Documents

- [Operating model](operating-model.md)
- [Transparency rules](transparency-rules.md)
- [Project Memory](project-memory.md)
- [Stable HACS releases](hacs-release-workflow.md)
- [Verification](verification-and-efficiency.md)
- [Agent orchestration](agent-orchestration.md)
- [GitLab retirement checklist](../operations/gitlab-retirement.md)

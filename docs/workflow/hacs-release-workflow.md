# Direct GitHub HACS release workflow

For every decided Home Assistant/HACS integration implementation, this release
path is part of the same assignment as implementation, tests, review, pull
request, and server-side merge. There is no separate follow-up assignment or
Benni approval gate between those steps. This is the process decision from
[control#15](https://github.com/Levtos/control/issues/15), clarified for agent
bootstrap in [control#50](https://github.com/Levtos/control/issues/50).

The direct release path is GitHub-native:

1. Run focused tests and review the scope and diff.
2. Open the pull request with the stable manifest version required by the
   repository rules and inspect all checks.
3. Merge the pull request server-side and verify the resulting default-branch
   SHA.
4. Create a matching `vX.Y.Z` tag on that verified merge SHA through the
   repository's approved path.
5. The repository's GitHub Action validates tag and manifest versions.
6. The Action creates or verifies a normal, non-draft, non-prerelease GitHub
   Release.
7. Verify the GitHub tag, release, and manifest.
8. Read HACS state, document the visible update or equivalent release evidence
   on the Issue, and hand the work over in `Testing`.

Stop before merge or release only when the assignment is explicitly read-only,
an audit, planning, or decision clarification; a concrete technical or product
blocker exists; checks fail; Benni explicitly stops that assignment; or a
repository rule requires another explicit approval. Document the blocker and
all incomplete steps. General caution is not a blocker.

The Action rejects pre-release suffixes by default. A pre-release requires an
explicit Benni decision and a separately documented workflow invocation.
Existing stable tags and releases are never deleted or replaced.

Repository-local tests remain separate from this release workflow. Public
GitHub Actions must not print runtime data, credentials, or private
configuration.

Merge, tag, GitHub Release, and HACS visibility are technical distribution
steps. They are not HACS installation, Home Assistant deployment, reload,
restart, `Live`, or `Live Verified`; Benni owns those later gates. Repositories
that do not publish a HACS release, including documentation-only governance
changes in `control`, stop after their repository-specific checks and
server-side merge.

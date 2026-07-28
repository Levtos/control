# Direct GitHub HACS release workflow

The direct release path is GitHub-native:

1. Merge the PR into the repository default branch.
2. Update the integration manifest to a stable patch version.
3. Create a matching `vX.Y.Z` tag on the verified merge SHA.
4. The repository's GitHub Action validates tag and manifest versions.
5. The Action creates or verifies a normal, non-draft, non-prerelease GitHub
   Release.
6. Verify the GitHub tag, release, and manifest.
7. Read HACS state and document the visible update on the Issue.

The Action rejects pre-release suffixes by default. A pre-release requires an
explicit Benni decision and a separately documented workflow invocation.
Existing stable tags and releases are never deleted or replaced.

Repository-local tests remain separate from this release workflow. Public
GitHub Actions must not print runtime data, credentials, or private
configuration.

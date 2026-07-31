# Release and rollback

Stable releases are the default. The normal path is:

Issue → PR → checks → server-side merge → manifest patch version → `vX.Y.Z`
tag → GitHub Action → normal GitHub Release → visible HACS update.

Alpha, beta, RC, and other pre-releases require an explicit Benni decision.
`status/testing` is not a pre-release signal.

Rollback uses an existing stable tag or a normal revert PR followed by a new
patch release. Never delete or replace an existing tag or release and never
force-push a protected branch.

## Platform source boundary

GitHub is the only active and historical code, Issue, Project, PR, Action, tag,
release, Project Memory, and HACS source of truth. GitLab, Plane, and Forgejo
are retired and are not valid alternatives, archives, or rollback targets.
Migration records may retain sanitized links as non-authoritative provenance;
they never define a recovery path.

The rollback path is therefore GitHub-native: use an existing stable tag or a
normal revert PR, then publish a new patch release when the affected repository
is a HACS integration. Never delete or replace an existing tag or release and
never force-push a protected branch. Home Assistant restores and downgrades
remain separate live-system actions behind Benni's gate.

No release, tag, mirror, service, repository, or live system is changed by
this documentation decision.

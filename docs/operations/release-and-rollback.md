# Release and rollback

Stable releases are the default. The normal path is:

Issue → PR → checks → server-side merge → manifest patch version → `vX.Y.Z`
tag → GitHub Action → normal GitHub Release → visible HACS update.

Alpha, beta, RC, and other pre-releases require an explicit Benni decision.
`status/testing` is not a pre-release signal.

Rollback uses an existing stable tag or a normal revert PR followed by a new
patch release. Never delete or replace an existing tag or release and never
force-push a protected branch. GitLab remains an untouched rollback/archive
copy while the cutover is verified.

# Release and rollback

Stable releases are the default. The normal path is:

Issue → PR → checks → server-side merge → manifest patch version → `vX.Y.Z`
tag → GitHub Action → normal GitHub Release → visible HACS update.

Alpha, beta, RC, and other pre-releases require an explicit Benni decision.
`status/testing` is not a pre-release signal.

Rollback uses an existing stable tag or a normal revert PR followed by a new
patch release. Never delete or replace an existing tag or release and never
force-push a protected branch.

## GitLab archive and mirror rollback

GitHub is now the active code, Issue, Project, PR, Action, tag, release,
Project-Memory, and HACS source of truth. GitLab is retained as a historical
archive and provisional rollback target. New work and releases do not start
there. Existing GitLab data remains available and was not deleted or
rewritten.

The former GitLab-to-GitHub bridge consisted of GitLab Remote Mirror objects
configured by the server-side helper
`/usr/local/sbin/configure-gitlab-github-push-mirror`. On 2026-07-29 only the
`enabled` property was set to `false`; no repository refs, tags, releases, or
Home Assistant services were changed. The mirror objects remain present so
that rollback is reversible by an authorized operator using the same
project/mirror pair and restoring `enabled=true`; a sync is not part of the
rollback declaration and must be evaluated against current GitHub state first.

| GitLab project | Project ID | Mirror ID | GitHub target |
|---|---:|---:|---|
| `title-classifier` | 3 | 1 | `Levtos/Title_classifier` |
| `media-art-wrapper` | 4 | 2 | `Levtos/Media_Art_Wrapper` |
| `core-devices` | 5 | 3 | `Levtos/benni-core-devices` |
| `core-state` | 6 | 4 | `Levtos/benni-core-state` |
| `blind-policy` | 7 | 5 | `Levtos/benni_blind_policy` |
| `climate-policy` | 8 | 6 | `Levtos/benni_climate_policy` |
| `door-policy` | 9 | 7 | `Levtos/benni_door_policy` |
| `light-policy` | 10 | 18 | `Levtos/benni_light_policy` |
| `media-core` | 11 | 8 | `Levtos/benni_media` |
| `media-apply` | 12 | 9 | `Levtos/benni_media_apply` |
| `media-context` | 13 | 10 | `Levtos/benni_media_context` |
| `media-policy` | 14 | 11 | `Levtos/benni_media_policy` |
| `media-state` | 15 | 12 | `Levtos/benni_media_state` |
| `notification-router` | 16 | 13 | `Levtos/benni_notification_router` |
| `scene-presets` | 17 | 14 | `Levtos/benni_scene_presets` |
| `discord-game` | 18 | 19 | `Levtos/discord-game` |
| `wake-planner` | 19 | 15 | `Levtos/ha_wake_planner` |
| `plug-policy-engine` | 20 | 16 | `Levtos/plug_policy_engine` |
| `stash-integration` | 21 | 17 | `Levtos/stash-ha` |
| `core-contracts` | 22 | 21 | `Levtos/benni-core-contracts` |

The mirror token remains server-side and is not reproduced here. LXC 104,
MCPHub, Home Assistant, and LeanCTX are not part of the GitHub cutover.

The next real, fully decided integration fix is the operational release
confirmation. No artificial code change, patch tag, release, or HACS refresh
is created for this cutover. If that normal run exposes a technical error,
the responsible GitHub Issue remains the place for diagnosis and repair; it
does not automatically restore GitLab as primary.

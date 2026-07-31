# GitHub cutover evidence

Date: 2026-07-29

## Actors

The current technical GitHub access is a single authenticated account:

| Operation | Verified actor |
|---|---|
| GitHub API / gh | Levtos |
| Git clone/fetch/push | authenticated GitHub transport as Levtos |
| Commit author in the cutover PRs | Codex Agent <codex-agent@github.local> |
| Push actor | Levtos |
| PR creator | Levtos |
| Server-side merger | Levtos |
| Workflow actor | not exercised by this cutover; next real stable release uses GitHub Actions |
| Release actor | not exercised by this cutover; next real stable release uses GitHub Actions |

The commit author is intentionally documented separately from the push, PR,
merge, workflow, and release actors. No separate Claude or ChatGPT GitHub
identity is currently available. No identity or token was created or changed
by this cutover.

## Preflight

- GitHub account: Levtos.
- Repository admin permission: verified on public repositories.
- Git fetch: verified.
- GitHub push dry-run: verified from a fresh GitHub clone.
- Issues: creation and label assignment verified; 38 issues imported.
- Pull requests: creation, readback, and server-side merge verified.
- Actions: workflow definitions and existing releases readable.
- Releases/tags: API access readable; no new release or tag created.
- Project: Project `Platform Workflow` is readable and writable as
  `PVT_kwHOBbFWO84Beupq`, with 38 imported Issues and the documented fields and
  views.
- Branch protection: PUT succeeded for control and all 20 active integrations.
- Local dirty worktrees: not touched. All cutover changes used fresh clones
  under .codex-worktrees/github-cutover-repos.
- LXC 104, MCPHub, Home Assistant, and LeanCTX: outside this cutover and not
  changed. The former GitLab mirror state is recorded below as one-time
  cutover evidence only; it is not an active source, archive, or rollback path.

## Foundation

The public control repository was initialized from a bootstrap branch because
an empty GitHub repository had no PR base. The identical main ref was then
created as the initial baseline. Subsequent changes use PRs.

- Repository: https://github.com/Levtos/control
- Bootstrap commit: 4bfd39c0dd7bdd88db11910430114b83b3052243
- Initial main ref: 4bfd39c0dd7bdd88db11910430114b83b3052243
- Contents: sanitized README, AGENTS, CLAUDE, docs, templates, tests, helper,
  and reusable stable-release workflow.
- Excluded: Plane CSVs, historical exports, live configuration, secrets,
  private keys, active topology, old test pages, and obsolete GitLab/Forgejo
  instructions.

## Repository bootstrap PRs

Each PR changed only AGENTS.md, CLAUDE.md, and the minimal shared HACS caller.
The listed commit is the agent commit; merge SHA is the server-side result.

| Repository | PR | Commit | Merge SHA |
|---|---:|---|---|
| Levtos/Title_classifier | 75 | 0fa9e9d5803c1cadbd971bfe857639002331a56a | 744f89be66ca8ab91f987dcdcacf3ed95c30959b |
| Levtos/Media_Art_Wrapper | 56 | 7abea63bf25ae7d177886e4b6f4619568bc63bd9 | d294f38157625e6509d232063d546abcb222ff42 |
| Levtos/benni-core-devices | 32 | e7663353b72ea4f168673a2daf9104fc3063c13a | bd0031315df5b23f92794254f75795cf7cf11f9d |
| Levtos/benni-core-state | 17 | 7e438c74c843992378cf4c6431e772252272ee87 | 6b40e5d149aecb8a0386e9334a2c75537691225c |
| Levtos/benni_blind_policy | 5 | 3b38098e45a6de9c85d4d1a26ed9227215754083 | a45264b887d1f5ce7dd67d7f92b825e373a85151 |
| Levtos/benni_climate_policy | 25 | f1b8ce54dc1f9ac75db70992f981b1f6e47a4218 | 56a266cc6e4a81303ec837537838845bf3b933d1 |
| Levtos/benni_door_policy | 12 | f0b55ee7061c9a4e5840da670ca147940f3f2fe2 | 66b0f2564bcc76e554cfbcaa71226bd888c329ae |
| Levtos/benni_light_policy | 17 | 426da45101a4d19fc95f9fbac0e34d2edcc4cced | 4f8dc8db3f47cea8c8dd787328992a5129984e15 |
| Levtos/benni_media | 9 | 5020738b774c62121a7569a303c57a8b5cade497 | 508591a88468930b07f59fbc437ab1439ab82d91 |
| Levtos/benni_media_apply | 25 | 00578021e0bf1b5f1e3649d475566f02178b03f0 | 31552f5f35c38f617d5b3167190533772e25602a |
| Levtos/benni_media_context | 1 | d08de979340effbbf9c4ee96de92996875f2f05e | 8aa04201086a198e305ea9ef7ec3a62df1599968 |
| Levtos/benni_media_policy | 23 | d1d8927acd5f26e8f5471683e5695efc95a91fac | 19b3dfb8186083484381fb3c305fddf2c4f617c4 |
| Levtos/benni_media_state | 16 | 8944b523fc0ee6dbf2b84b98db90352e11d57dd6 | 79c63ddfe9ee3719132b95e923146e84fc5a7187 |
| Levtos/benni_notification_router | 1 | b34e416cf9b973e8fa3be60a6c6f383cbe41906d | f3094603f15a9316dcdb1cbec899b1be38d8a2a7 |
| Levtos/benni_scene_presets | 26 | b0530e9493bfaf1b2fd0a196fb48bd4e91d3d634 | 743c542f6ea66312e13dccc3d39b67bfa7b8ba1a |
| Levtos/discord-game | 1 | 223a7313887019fcbf6dfab77007abfb735ad598 | 8c807eb5540b518f3949ed15c11a9d3d46b56e87 |
| Levtos/ha_wake_planner | 31 | 83d14295a86411e2b98e748d5ae1b228cd49eff0 | cf26d59766ed11ae24896a1a9b13b98ea3ecb87d |
| Levtos/plug_policy_engine | 14 | eabb093986df1cdc835a0e84f1dc907e22f7251c | 4cd73190b7fec7fef3334857a0937d53e507ba88 |
| Levtos/stash-ha | 32 | 9f79bbb40f8af8cb724a6588df8cfaca0f604505 | b8f1699d5bfcd5c15416e354735f1e5e090d175e |
| Levtos/benni-core-contracts | 3 | a822de7d8a12ac08c4e0fdbaa1994a3dff90ff4d | f3d9995cca05a1f5f029dbb85793f6f3718023ec |

## Branch protection

Minimal protection is active on control/main and the default branch of every
active integration. It requires pull requests, disallows force-pushes and
branch deletion, enforces the rule for administrators, and requires no
non-existent status checks or human approval count. This preserves the
agent-led server-side merge flow while preventing direct default-branch pushes.

## Release state

No version, tag, or release was created by this foundation batch. The direct
stable-release workflow is installed. An artificial release or HACS test is
not required: previous platform work already exercised and verified GitHub
Releases and HACS delivery. The next real, fachlich decided integration fix
will use the direct GitHub release path as normal operational confirmation.
An error in that run is handled in its GitHub Issue and does not change the
GitHub-only source-of-truth decision. Existing stable releases and
prereleases were not changed.

## Mirror state

The former active distribution bridge was the GitLab Remote Mirror API, not
MCPHub itself. The 20 per-project mirror objects were disabled with
`PUT /projects/:id/remote_mirrors/:mirror_id` and `enabled=false`; the mirror
objects, target mappings, server-side credentials, GitLab repositories, tags,
Issues, and releases were not deleted. The mirror IDs and project IDs are
listed in `docs/operations/release-and-rollback.md`.

All 20 mirrors read back as disabled after the operation. The
`title-classifier` mirror retained a historical failed-status flag and a
successful-last-run timestamp; its error text is intentionally not copied
into repository documentation.

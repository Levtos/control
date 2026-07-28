# GitHub Project: Platform Workflow

The active cross-repository workflow Project is owned by `Levtos`.

- Project URL: <https://github.com/users/Levtos/projects/1>
- Project number: `1`
- Project ID: `PVT_kwHOBbFWO84Beupq`
- Created and verified: 2026-07-28

## Fields

The field IDs below are GitHub Project metadata, not credentials.

| Field | ID | Type | Options |
|---|---|---|---|
| Status | `PVTSSF_lAHOBbFWO84BeupqzhZGsCg` | single select | Backlog `778d9a33`; Ready `d8785592`; In Progress `b465fa4e`; Testing `a9899e7c`; Live `b6c75379`; Blocked `6e478966`; Archived `7f45d52f` |
| Type | `PVTSSF_lAHOBbFWO84BeupqzhZGu04` | single select | Idea `b0a9e762`; Feature `4aa6d692`; Bug `4a1d97b8`; Decision `156e29c0`; Refactor `ce15a981`; Chore `af8d6e57`; Docs `5260cd56` |
| Priority | `PVTSSF_lAHOBbFWO84BeupqzhZGu08` | single select | Now `83e37003`; Next `ee5a67bb`; Later `e9b56b11`; Parking Lot `7ddf28fe` |
| Owner | `PVTSSF_lAHOBbFWO84BeupqzhZGu14` | single select | Benni `4b8cc1ec`; ChatGPT `f7678305`; Codex `79b3d058`; Claude `8e237f89` |
| Scope | `PVTSSF_lAHOBbFWO84BeupqzhZGu18` | single select | Benni `1f33fe10`; Eltern `a284d28a`; Platform `563e55b9`; Cross-Repo `f089f10e` |
| Evidence | `PVTSSF_lAHOBbFWO84BeupqzhZGu2A` | single select | Missing `394f37a9`; Tests Pass `3bebe7d0`; Live Verified `324eb516` |
| Module | `PVTF_lAHOBbFWO84BeupqzhZGu2E` | text | free text |

## Views

| View | Number | ID | Layout |
|---|---:|---|---|
| Platform Workflow | 2 | `PVTV_lAHOBbFWO84BeupqzgLHxoo` | board |
| Ideas & Features | 3 | `PVTV_lAHOBbFWO84BeupqzgLHxos` | board |
| Agent Work | 4 | `PVTV_lAHOBbFWO84BeupqzgLHxo4` | board |
| Decisions | 5 | `PVTV_lAHOBbFWO84BeupqzgLHxo8` | table |
| Benni | 6 | `PVTV_lAHOBbFWO84BeupqzgLHxpE` | table |
| Eltern | 7 | `PVTV_lAHOBbFWO84BeupqzgLHxpI` | table |

## Import rule

The 38 Issues listed in `docs/migration/github-issue-mapping.md` were added
to this Project. Status, Type, Owner, Scope, and Evidence were copied only
from the corresponding GitHub Issue labels. Priority and Module were not
inferred and remain unset.

`Scope` is a single-select field. When an Issue has the explicitly evidenced
`scope/cross-repo` label, the Project value is `Cross-Repo`; otherwise a
single recognized scope label is copied. Issues that only have the legacy
`scope/shared` label remain unset because no equivalent Project option was
approved.

New Issues should be created and added through `tools/github_workflow.py`:

```text
python tools/github_workflow.py issue-create --repo Levtos/control --title "..." --body "..." --project-id PVT_kwHOBbFWO84Beupq --type Chore --owner Codex --scope Platform
```

The helper defaults new work to `Status=Backlog` and `Evidence=Missing`,
requires Type, Owner, and Scope, reuses an exact existing title, adds the
Issue idempotently, sets only explicitly supplied optional Priority and
Module values, and emits structured JSON. It does not require or print a
token.

# GitLab to GitHub Issue mapping

The historical source is `ha-platform/control`; no GitLab Issue number is
reused as a GitHub Issue number. Every imported Issue must retain the source
URL and only sanitized, still-relevant decisions/evidence.

| GitLab | GitHub target | Current status/type/owner/scope/evidence |
|---|---|---|
| #64 | `Levtos/control` | in-progress / chore / Codex / Cross-Repo+Platform / Missing |
| #51, #49, #32, #41, #18, #8, #16 | `Levtos/control` | preserve each source state; sanitize private targets |
| #62, #55, #53, #52, #27 | `Levtos/Title_classifier` | preserve source metadata and live gates |
| #57, #59 | `Levtos/benni-core-contracts` | Testing / feature / Codex / Platform / Missing or Tests Pass |
| #56, #5, #6, #13 | `Levtos/benni-core-devices` | preserve source metadata; do not infer priority |
| #42 | private parents configuration reference | sanitize; keep private topology out |
| #54 | `Levtos/stash-ha` | In Progress / feature / Codex / Benni / Live evidence requires review |
| #50, #35 | `Levtos/plug_policy_engine` | preserve source metadata |
| #48, #46, #44 | private `einhornzentrale` reference | sanitize and keep configuration private |
| #45 | `Levtos/benni_media_policy` | Testing / bug / Codex / Cross-Repo / Tests Pass |
| #37, #47, #12, #4 | `Levtos/benni_door_policy` | preserve safety gates |
| #63, #28 | `Levtos/benni_media` | preserve decision/live gates |
| #15, #14, #10 | `Levtos/benni_light_policy` | preserve source metadata |
| #9 | `Levtos/benni_climate_policy` | preserve source metadata |
| #11 | `Levtos/benni_blind_policy` | preserve source metadata |

The following remain historical or are consolidated rather than imported as
separate active Issues: #60 into #62, #61 into #63, #17 into the UX ADR, #58
into the UX ADR, and completed Issue #3 into durable documentation.

Priority and Module are left unset when the GitLab evidence does not support
them. The four status/evidence inconsistencies found in the audit must be
documented before any import is treated as complete.

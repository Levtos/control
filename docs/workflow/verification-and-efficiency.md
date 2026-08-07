# Verification and efficiency

Versioned workflow rule: 2026-08-07, [control#33](https://github.com/Levtos/control/issues/33)
and the [control#17 Shadow-DOM addendum](https://github.com/Levtos/control/issues/17#issuecomment-5218335273).

## Evidence proportional to the claim

Use the smallest evidence that establishes the requested technical claim and
keep time and token effort proportional to the risk and the reachable proof:

- `git diff --check` and focused repository tests for code changes;
- PR checks and the current merge SHA for server-side integration;
- tag, manifest, release type, and Action run for a release;
- read-only HACS state for visible availability;
- live HA behavior only for the explicit human Live gate.

Standalone demo pages, mock hosts, screenshot collections, and new browser or
Shadow-DOM harnesses are not standard UX deliverables. Create them only when
the Issue explicitly requires the artifact or when a concrete, reproducible
technical claim cannot otherwise be checked. They must not become a blanket
Merge- or Release-Gate.

## Embedded UX and Shadow DOM

For an embeddable module, styles must be loaded within the actual module or
Shadow-Root boundary; they must not be provided exclusively through
`document.head`. Global selectors such as `:root` and `body` are scoped to
`:host` or to an unambiguous module-internal root so styles do not leak into or
depend on the host page. A standalone Vite preview is not evidence of the
Home-Assistant panel boundary unless the Issue explicitly makes that preview
the target.

## Normal HACS and Live-gate sequence

When no separate HA test environment exists, the normal technical sequence is:

1. Run focused repository checks.
2. Open a PR and inspect its current checks and mergeability.
3. Merge server-side and record the merge SHA.
4. For HACS work, publish a matching stable manifest/tag through the existing
   release Action and verify the normal release.
5. Verify HACS-visible availability read-only and document the evidence.
6. Benni creates his backup, pulls the version, and performs the real HA test.

An Issue agent does not wait for extra micro-approvals for ordinary branch,
commit, PR, merge, tag, or release steps already decided by the Issue. Merge,
release, and HACS visibility remain `Testing`; only Benni sets `Live` or
`Live Verified` after the real HA check.

If the live check fails, use a normal fix PR and a new patch release. Existing
stable tags and releases are never replaced or deleted, so rollback remains
available through the previous version.

## Recording evidence

Do not infer a merge, release, deployment, or live result from a local commit
or successful push. Record exact URLs, IDs, timestamps, actors, and workflow
run IDs without secret values. Repository-local tests and central release
automation are separate layers; do not add a runner, CI gate, or test
infrastructure unless the Issue requires it.

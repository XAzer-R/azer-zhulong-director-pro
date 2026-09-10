# Review receipts

[简体中文](../REVIEW-RECEIPTS.md) | English

After an actual review, the coordinator saves a JSON receipt inside the selected work's output directory. It must contain:

| Field | Meaning |
|---|---|
| `status` | `PASS` or `FAILED` |
| `blockers` | An array of unresolved issue strings; must be empty to continue |
| `inputs` | Relative input file paths mapped to their actual lowercase SHA-256 digests |
| `outputs` | Relative output file paths mapped to their actual lowercase SHA-256 digests |

Both version-binding objects must contain at least one real file. Do not use example digests or claim PASS without a review.

For a director project, run from the repository root:

```shell
python -B tools/workflow_guard.py review outputs/review.json --root .
```

For a screenplay work, use its own root and a receipt path relative to that root:

```shell
python -B tools/workflow_guard.py review review.json --root projects/my-story
```

The latter command assumes you actually saved `projects/my-story/review.json`.

- `CURRENT`: current versions match a passing receipt; exit 0.
- `BLOCKED`: the review failed or blockers remain; exit 1.
- `STALE`: a bound file changed or is missing; exit 1.
- Invalid data or inaccessible paths: exit 2.

These receipts are local consistency records, not signed approvals. A user with write access can change them. Hashes do not prove artistic quality or replace the responsible reviewer.

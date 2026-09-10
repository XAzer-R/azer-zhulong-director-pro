# Runtime contract

[简体中文](../RUNTIME-CONTRACT.md) | English

This is the English translation of the shared runtime contract. The existing host entry continues to load the Chinese source. Neither translation nor language choice grants additional permissions.

## Entry points and context

- Claude Code loads the root CLAUDE.md and the main workflow in .claude/CLAUDE.md. Inputs such as `~start` and Chinese slash-style phrases are project conversation conventions, not installed shell or host commands. Use ordinary language if the host intercepts them.
- Work on one selected project, episode, or segment at a time. Every delegation specifies the system root, work root, target unit, exact inputs, permitted output paths, and current versions. A child agent must not rely on unprovided parent conversation context.
- Resolve method files relative to the system root and work inputs/outputs relative to the selected work root. Do not save a screenplay or private source material inside a Skill directory.
- If the host cannot load or delegate a role, report that limitation. Do not simulate independent review while describing it as a real independent agent run. Keep self-review and independent review distinct.
- The user and host choose the model. Platform notes describe prompting methods, not guaranteed current API support, duration, resolution, access, or prices.

## State and revisions

- A file's presence is not a passing result. Continue only when input and output versions match the review, its status is PASS, and it has no blockers.
- Allow at most two automatic revision rounds. If the result still fails, retain FAILED / NEEDS_USER_DECISION and list unresolved issues. Exhausting a budget or retry count never converts a failure into a pass.
- Changes to a screenplay, cinematography agreement, identity reference, or keyframe invalidate dependent reviews. Identify affected units and review the current versions again.
- Before revising completed work, show scope and differences and preserve a recoverable prior version. Use one writer for each file at a time.
- The director owns production content. Art and storyboard roles return asset IDs and proposed bindings. Only the coordinator updates the upload list and asset mapping after checking them; it does not change the director's dialogue, shots, action chain, or generation mode.
- If actual reference images do not exist, mark assets as pending. Completed design does not mean images, videos, or a finished film have been generated.

## Empty projects and optional inputs

- Start with configuration when no work exists; do not invent a pre-existing story. The user supplies or confirms the work type, visual direction, and creative scope.
- Empty templates and `status: unconfigured` mean not configured, even if the files exist.
- Missing optional examples, prior episodes, or old review logs should be reported and skipped. Missing required inputs, such as the current screenplay, stop that stage.
- Example paths refer to future user-created files. The package supplies blank templates, not completed productions.

## Permissions and costs

- Default to text planning, review, and file maintenance within the selected project. Paid APIs, media generation, uploads, publishing, and destructive operations require applicable user authorization.
- Do not scan local credentials, install hooks, read unrelated private work, switch providers after failure, or automatically replay paid requests.
- Stop business execution when the user asks to pause or finish, and state the exact stopping point.

## Mechanical checks

Validate a real unit identifier before dispatch:

```shell
python -B tools/workflow_guard.py unit EP01-S01
```

After a review, save a receipt following [Review receipts](REVIEW-RECEIPTS.md). Run the review checker before downstream work. Any nonzero exit code prevents progression. Run the tool from the system root and set `--root` to the selected work root.

## Language

Use the user's requested language for conversation, explanations, and newly created creative content. Preserve existing screenplay dialogue unless translation or rewriting was requested. File paths, commands, identifiers, JSON keys, and status codes remain unchanged. Some technical formats and underlying Skill instructions are still Chinese; do not rename their fields merely to translate the output.

# Optional Blender workflow

[简体中文](../BLENDER-GUIDE.md) | English

## Start

1. Install and configure Blender yourself. This repository does not install software or enable plugins automatically.
2. Run `python -B tools/blender_preflight.py` from the repository root. Use `--binary` to specify an existing Blender executable if it is not on PATH.
3. In Codex, invoke `$blender-director`. In Claude Code, ask the coordinator to use `blender-artist`.
4. Specify the modeling subject, scale, allowed edit scope, and intended deliverable. Explicitly authorize scene execution when you want it performed.
5. Read back objects and output files and inspect the actual result. Successful script exit is not a visual quality check.

## Modes

- **Greybox/blocking:** placement, support surfaces, interaction direction, waiting versus moving, camera framing, and key motion phases.
- **Basic modeling:** decompose a subject into structure, parts, connections, and dimensions before increasing complexity.
- **Camera/motion changes:** operate on selected objects or a dedicated collection and inspect visibility, occlusion, and trajectories.

The shared Skill lives at `.claude/skills/blender-director/SKILL.md` and remains Chinese. The Codex wrapper points to that same source. Ask your model to explain and work in English while preserving technical field names.

## What is included

Operating methods, host entry points, a read-only version probe, and lessons from the author's earlier greybox practice. No legacy production engine, hardcoded character/prop mapping, demo film, machine-specific path, MCP installation, or third-party download configuration is included.

Use a fresh background process for isolated work. For live editing, inspect and modify only the selected scope. Never clear every object from the user's open scene. Only the coordinator can apply reviewed asset bindings back to production cards.

## Evidence and limits

The original local version probe returned Blender 5.1.2. It only ran `--version`; it did not model or render. Tests cover missing executables, process errors/timeouts, version-only invocation, host wrappers, and optional routing.

Real modeling, rendering, live MCP changes, model calls, and the effect of greybox references on final video generation have not been verified for this release. The Blender-specific Codex entry does not imply full Codex support for all director roles.

## Reference documentation

- [Blender Python API](https://docs.blender.org/api/current/)
- [Blender command-line arguments](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)
- [Codex Skills](https://learn.chatgpt.com/docs/build-skills)

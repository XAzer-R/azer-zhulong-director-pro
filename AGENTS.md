# 阿泽 AI导演专业版｜烛龙造境

维护本系统时先读 `docs/RUNTIME-CONTRACT.md` 与 `.codex/WIP.md`。本项目的原生角色配置面向 Claude Code；其他宿主可以参考方法，但没有完成同等自动发现或调度验收。

只将通用角色、技能、工具、空白模板与说明纳入 Git。作品、原始参考、凭据与运行态默认忽略。修改工作流后运行 `python -B tools/validate.py` 和 `python -B -m unittest discover -s tests`。

实际创作使用 `.claude/CLAUDE.md` 的入口和相对路径；不能将维护动作与作品制作混为一轮。


## Codex Blender 入口

用户要求 Blender 建模或白模预演时，按需读取 `.agents/skills/blender-director/SKILL.md`，使用其指向的统一正文。该专项可由当前主 Agent 执行，不要求 Claude 角色注册；普通导演三阶段仍没有完整 Codex 原生适配保证。

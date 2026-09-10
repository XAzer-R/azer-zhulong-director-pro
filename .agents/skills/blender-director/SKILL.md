---
name: blender-director
description: 在 Codex 中按需使用 Blender 建模、白模灰模预演、人物占位走位与摄影机调整方法。读取仓库内的统一技能正文，不依赖 Claude 的 Agent 注册。
---

# Blender 按需入口

从本文件所在目录向上三级得到系统根。先读取系统根 `docs/RUNTIME-CONTRACT.md`，再读取 `.claude/skills/blender-director/SKILL.md`；该文件是唯一方法正文，随包附带，不需要外部仓库。

本入口可由当前 Codex 主 Agent 执行，不要求安装或调用 `.claude/agents/blender-artist.md`。是否委派遵循宿主及用户指令，不能声称 Claude 角色已自动注册到 Codex。

模型由用户当前会话选择；本包没有模型版本 pin。读完技能后先核对用户要求的是方案、建模执行还是预演，不自动进行媒体生成。

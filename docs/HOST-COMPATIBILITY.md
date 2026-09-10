# 宿主与验证范围

原生文件布局面向 Claude Code：根 CLAUDE.md 导入运行合同和主控，角色在 .claude/agents，技能在 .claude/skills。

官方配置参考：[项目记忆与导入](https://code.claude.com/docs/en/memory)、[子 Agent 与 skills](https://code.claude.com/docs/en/sub-agents)。

其他宿主可阅读这些方法，但本发行版不提供 Codex/WorkBuddy 的自动角色注册或跨宿主一致性承诺。AGENTS.md 服务于仓库维护，不等于已完成其他宿主适配。

离线验证检查文件、元数据、输入边界及审核状态策略；没有进行真实模型创作、独立子 Agent 调度、图像或视频生成。若宿主无法调度角色，必须报告不支持，不能模拟独立审查。

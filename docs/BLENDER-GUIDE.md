# Blender 操作与白模经验

## 快速开始

1. 安装并自行配置 Blender；本仓不自动下载、安装或启用插件。
2. 在项目根执行 `python -B tools/blender_preflight.py`。不在 PATH 时传 `--binary` 指定现有程序。
3. Codex 使用 `$blender-director`，或请主控“用 Blender 先做空间方案”；Claude Code 可按需调用 blender-artist。
4. 说明建模对象、比例、修改范围和期望交付。需要真实执行时明确本次执行范围。
5. 操作后回读对象和文件并进行视觉检查，不能用脚本退出成功替代模型质量验收。

## 继承与调整

保留：复杂镜头优先预演；人物/场景关系先于细节；驻留与走位分离；交互朝向；支撑与遮挡；关键相位先回看；已知近似显式说明。

调整：从特定作品引擎改为通用 Blender 方法；从全场清空改为限定对象/Collection；从固定本机路径和端口改为显式探测；从模型名绑定改为用户选择；production 仍由导演/主控持有。

排除：旧角色、场景和按段号兜底映射、内置 demo、原作品产物、机器绝对路径、MCP 安装配置和第三方素材下载。BlenderMCP 是可选外部工具，没有复制其代码或许可证到本包。

## 当前证据

本机 `--version` 回读为 Blender 5.1.2；这只证明当前程序可启动返回版本。单元测试覆盖缺失程序、失败与超时、仅请求版本、两宿主入口和按需路由。

本次未执行真实建模、渲染、MCP 场景修改或模型调用；未验证白模视频对最终视频模型的控制效果。旧经验中的 Blender 版本差异仍需使用时查当前官方 API。

## 官方入口

- [Blender Python API](https://docs.blender.org/api/current/)
- [Blender 命令行](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)
- [Codex Skills](https://learn.chatgpt.com/docs/build-skills)

Codex 新增的只是 Blender 专项 Skill，不表示原三角色导演流程已完成 Codex 端到端适配。

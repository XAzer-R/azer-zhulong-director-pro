# Blender 执行与回看

## 规划

- 先决定新建独立文件还是调整用户当前场景。live 修改前记录选定 Collection、对象和文件版本。
- 建模单位、轴向、对象原点、应用缩放与父子关系应先确定；几何细化之前先验证结构。
- 优先使用 bpy.data 的明确数据操作；依赖编辑模式或视口上下文的 bpy.ops 操作必须检查 context 和 mode。
- 相机方向、镜头焦距和目标点分开记录。不要通过随意改焦距补救错误的世界尺度。

## headless

命令形态如下，路径由本次任务实际解析：

```text
blender --background --factory-startup --disable-autoexec --python-exit-code 1 --python <reviewed-script.py> -- <task-input.json>
```

不传入未知 blend 文件；不让输入 JSON 携带任意 Python。非零退出码视为失败，不能因为有旧文件存在而宣称成功。长任务输出保存到本次输出目录的日志，不通过截断管道提前终止进程。

保存文件前拒绝覆盖已有目标，或按用户明确决定另存新版本。所有输出使用已核验的新目录与绝对路径；不要依赖 Blender 对相对路径的解释。

## live

先只读查看当前场景与工具能力，再操作本次的专用 Collection。保持其他 Collection、插件、偏好和当前文件原样。不得使用旧引擎的“清空所有物体”方法。

MCP 是可选的宿主连接方式。本仓不包含或自动安装 BlenderMCP，也不假定本机已授权第三方资产下载。连接失败时报告，不自动更换端口或扩大网络监听范围。

## 回看与交付

建模检查至少包含：对象/部件数量、命名、单位与尺度、变换、法线、可见性、层级、相机取景及必要的碰撞/穿模检查。需要动画时检查关键相位和插值；静态尺寸检查不能替代运动验收。

请求保存 blend 时需要重新打开或用独立进程读取验证；渲染图要实际目检。视频要核对时长、帧率和可解码性，搜索 `ftyp` / `avc1` 字节不能证明视频有效。

Blender 版本变化会影响动画 Action 和视频导出 API。旧经验提到 slotted action、media_type 等差异，使用前按当前 API 核验，不固定照搬某个版本的设置顺序。

## 官方参考

- [Blender Python API](https://docs.blender.org/api/current/)
- [Blender 命令行参数](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)
- [Blender Python 快速入门](https://docs.blender.org/api/current/info_quickstart.html)

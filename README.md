# 阿泽 AI导演专业版｜烛龙造境

**在视频提示词主干上增加身份底图、材质光影与关键帧精修。**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg)](CHANGELOG.md)
[![Host](https://img.shields.io/badge/host-Claude_Code-orange.svg)](docs/HOST-COMPATIBILITY.md)

阿泽山海创作系列 · AI 影视创作工作流 · Agent / Skills / 提示词 / 空白模板

本项目提供可阅读、可修改的创作方法与角色协作规则。你提供自己的创作目标和授权材料，由主控组织分阶段执行、审核与修订。仓库不附带具体剧本、小说原文、图片、视频或历史创作产物。

## 三个项目怎么选

| 项目 | 适合的需求 | 流程 |
|---|---|---|
| [飞廉开镜](https://github.com/XAzer-R/azer-feilian-director) | 已有剧本，希望快速得到镜头与视频提示词 | 导演 → 服化道 → 素材引用回填 |
| [烛龙造境](https://github.com/XAzer-R/azer-zhulong-director-pro) | 已有剧本，希望进一步控制画面材质、光影与关键帧 | 导演 → 服化道 → 分镜师精修 → 主控回填 |
| [青丘织事](https://github.com/XAzer-R/azer-qingqiu-screenplay) | 从想法或授权改编材料开始写剧本 | 孵化 → 结构与人物 → 场景 → 独立审稿与修订 |

三个系统独立运行，不需要互相安装；剧本可作为导演系统的输入，由用户选择交接。

## 能做什么

- 导演 + 服化道 + 分镜师，三阶段流程。
- 18 个一级 Skill，按当前任务加载专业方法，避免无关内容堆进上下文。
- 明确角色读写边界、输入版本与审核状态；修改上游后重新核验下游结果。
- 自动修订最多两轮，仍失败就保留问题并交用户决定，失败不会被改成“通过”。
- 提供本地只读校验工具与回归测试，便于检查分发包是否完整。

## 环境要求

- 原生配置面向支持项目 `.claude/agents` 与 `.claude/skills` 的 Claude Code。
- 使用者自行准备宿主和模型访问权限；仓库没有账号、密钥、预付额度或模型权重。
- Python 3.10+ 只用于离线校验，不是运行创作提示词的必需依赖；校验工具无第三方 Python 依赖。
- 其他 Agent 宿主可参考或适配方法，目前没有跨宿主自动注册与端到端等价保证。

## 安装与首次使用

```shell
git clone https://github.com/XAzer-R/azer-zhulong-director-pro.git
cd azer-zhulong-director-pro
python -B tools/validate.py
claude
```

没有 Git 时也可通过 GitHub 的 **Code → Download ZIP** 下载解压，并在项目根启动宿主。不要双击 Markdown 期待自动安装；不要向聊天粘贴密钥。

根目录 `CLAUDE.md` 导入运行合同和主控。进入新会话后直接说明目标，例如：

```text
~start EP01
```

首次使用请先确认作品类型、视觉风格和目标媒介，再将自己的剧本放到 `script/EP01.md`。每段使用 `## S01 · 场景标题` 格式，编号在本集唯一。空摄影圣经不会被当作已配置。

| 对话入口 | 用途 |
|---|---|
| `~start EP01` | 本集第一个待处理导演单元 |
| `~start EP01-S01` | 指定段的导演设计与自审 |
| `~design EP01` | 本集导演阶段通过后设计身份素材 |
| `~status` / `~help` | 查看实际状态或入口说明 |
| `~render EP01-S01` | 身份设计通过后生成关键帧渲染卡 |

这些指令发送给主控，不是终端命令。提示词中的 @图N 是素材绑定编号，不是自动生成或上传的证明。

## 输入、输出与文件结构

```text
CLAUDE.md                  宿主入口
AGENTS.md                  仓库维护规则
.claude/CLAUDE.md           主控流程
.claude/agents/             角色合同
.claude/skills/             专业方法与空白模板
docs/                      运行合同、使用边界与检查报告
tools/                     只读验证工具
tests/                     隔离回归测试
project.json               发行元数据
```

剧本位于 `script/`，身份设计位于 `assets/`，段级 production 和渲染卡位于 `outputs/`。

作品目录默认被 Git 忽略。导演版少量已跟踪的空白 assets 模板填写后仍会出现在 Git 改动中；发布前必须检查差异，不能用 `git add .` 无差别提交作品。

## 验证与状态检查

```shell
python -B tools/validate.py
python -B -m unittest discover -s tests
python -B tools/workflow_guard.py unit EP01-S01
```

对实际审核记录可运行：

```shell
python -B tools/workflow_guard.py review outputs/review.json --root .
```

剧本系统应把 `--root` 指向当前 `projects/<项目名>`，回执路径相对该作品根。回执格式见 [审核记录](docs/REVIEW-RECEIPTS.md)。工具只验证当前文件版本与审核记录一致性，不证明艺术质量，也不是防篡改签名。

## 当前验证边界

本发行版完成的检查与发现见 [运行机制检查](docs/RUNTIME-REVIEW.md)。离线测试不等于真实模型创作成功；本轮没有调用模型、生成媒体或完成 Claude Code 全流程 E2E。因此本项目以 **0.1.0 工作流发行版**发布，不承诺一键出片或所有宿主开箱即用。

用户必须确认创作方向、处理剩余审核问题并自行管理素材权利。平台时长、分辨率和接口会变化，方法文件不构成平台能力保证。

## 贡献与反馈

欢迎提交明确的复现步骤、通用方法改进和兼容性补丁。请勿上传客户材料、完整小说、未授权影视帧、密钥或私人会话。

参见 [贡献指南](CONTRIBUTING.md)、[安全反馈](SECURITY.md) 和 [变更记录](CHANGELOG.md)。

## 作者与许可

作者：**阿泽（Azer）**。采用 [MIT License](LICENSE)，允许使用、修改和再分发，需保留版权与许可声明。第三方理论名称与方法参考见 [NOTICE](NOTICE.md)。

项目名称采用山海神话意象作为品牌命名，不宣称是古籍中的原句或职能定义。

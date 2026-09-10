---
name: production-template
description: 【指针·专业版】专业版分镜师不出 production（视频提示词）——production 由导演一次成型出 `<段号>-production.md`，权威格式在 director-skill 模板。分镜师据导演 production 渲染 @图N 精修关键帧（可读底 + 三道洗），回填进 production 喂 i2v 当首帧/参考，格式见 storyboard-template.md。本文件保留为指针，避免引用断裂。适配风格化生成与真人写实两条路线。
---

> Copyright (c) 2026 阿泽。依据根目录 LICENSE（MIT）使用。

# ⚠️ 本指针：production 是导演的产出，不是分镜师的

专业版 = 极速版 + 分镜师增强，**共用同一条视频主干**。production（视频提示词）由**导演**一次成型出 `<段号>-production.md`（提示词卡片：景别/运镜/驱动模式 + 分镜动作链 [C0N] + 台词内嵌 + 上传@图），结构与极速版完全一致，是用户在用的视频出口产出。

**导演 production 的权威格式模板**（不在本目录）：
> **`.claude/skills/director-skill/templates/director-analysis-template.md`**

**分镜师不出 production、不回写 production**——分镜师据导演 production 卡片的画面描述 + 服化道身份级底，**渲染 @图N 精修关键帧**（可读底 + 三道洗：质感→光影→氛围），回填进 production 的素材对应表，**喂导演 i2v 当首帧/参考**。

**分镜师产出的权威格式模板**：
> **`.claude/skills/storyboard-skill/templates/storyboard-template.md`**

它定义专业版 `<段号>-storyboard.md`（@图N 渲染卡）的输出格式：
- 文件头 + 段内总览 + 段级素材对应表（@图N·继承服化道身份级底）
- 每剧情点：每镜一张 @图N 渲染卡（可读底：镜次景别机位 + 画面瞬间 + 构图 + **风格前缀** + 上传素材 ‖ 三道洗：质感 → 光影 → 氛围 ‖ avoid + 回填去向）
- 段尾衔接（段尾画面 / 跨镜一致性提醒）+ 附·分镜师诊断

**专业版关键点**：
- ✅ @图N 是**生图**——**必写风格前缀**（取自 bible 风格前缀块）、**必写 avoid**（出图层面负面约束）
- ✅ @图N 是喂导演 i2v 的**精修关键帧**，回填进 production 素材对应表，**不取代、不回写 production**
- ❌ 分镜师**不写 i2v 视频提示词本体**：驱动模式（首帧/首尾帧/续写）、运镜、分镜动作链 [C0N]、时长档、模型、线稿——这些都由导演 production 写

@图N 渲染 + 逐层洗图方法论见 `storyboard-skill/SKILL.md`。

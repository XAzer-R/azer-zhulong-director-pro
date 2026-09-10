---
name: material-pbr-skill
description: 材质质感方法论（PBR·分镜师第一道洗）。让 @图N 关键帧从"CG 模型感/AI 味"升级为"被电影摄影机拍到的真实物体"——只升级材质/质感、绝不改几何结构。提供约束词、PBR 七要点（清漆菲涅尔/粗糙度变化/AO/GI/高光滚降/胶片颗粒）、反 AI 味纪律与可直接复制的中英提示词模板。**分镜师第一道洗（质感）时加载·质感归分镜师洗·服化道只出干净造型不焊质感**。尤其适合机甲 / 机械 / 金属 / 硬表面题材。适配风格化生成与真人写实两条路线。
---

> Copyright (c) 2026 阿泽。依据仓库根目录 LICENSE（MIT）使用。

# 材质质感方法论（PBR · @图N 关键帧生图层）

[技能定位]
    **主场 = 分镜师第一道洗（质感）**——分镜师在服化道身份级底（大平光锁内容）之上，第一道就用本 skill 洗质感，决定它是"CG 模型/AI 味"还是"被电影摄影机拍到的真实物体"。**服化道只出干净造型/结构（不焊质感）**，质感归分镜师洗；分镜师据 @图 + 本镜需要洗质感（含回洗服化道设定图补漏），产出 @图N 精修关键帧喂导演 production 的 i2v 当首帧/参考。**只作用于生图质感，不碰几何/构图/镜头**（那是导演 production 运镜/分镜动作链的事）。渲染型（CG/机甲/异形/硬表面）必洗；继承型（真人/真实场地）以真实参照照片打底、质感继承自真实照片再轻洗。

[核心理念（先认知，再写词）]
    - **质感决定"像不像真的"**。一个机甲像玩具还是像实拍道具，差别全在材质，不在加多少特效。
    - **反面教材**：把"非常有金属质感"改成"超级有金属质感"——这不是写提示词，这是"提需求给甲方"。堆形容词没用，要写**物理**。
    - **PBR（基于物理的渲染）的本质**：让材质和光之间的关系更像真的，而不是"像贴图画画一样简单加个高光"。
    - **终极目标**：从"CG 模型"变成"被拍摄到的真实物体"。最大差别是**细节**——不是加大划痕、大战损，而是"现实里肉眼不一定注意、但摄影机凑近看会有的小纹理"。
    - **反 AI 味铁律**：所谓"AI 味 / CG 感"，大多因为**画面太干净**——这种干净不真实。要刻意还原真实感。
    - **"有逻辑"纪律**：**脏要脏得有逻辑，旧要旧得有逻辑**。哪里新、哪里旧、哪里积灰、哪里常被擦——符合生活物理规律才真实。这是对 AI 的一种**约束**，不是随机做旧。

[第一块 · 约束词（锁住几何，只许升材质）]
    材质升级最大的风险是 AI 顺手改了结构。先用约束词锁死：

    **中文约束词模板**：
    ```
    仅限重着色 / 材质升级。
    不要改变几何结构、外轮廓、比例、姿态、装甲分块、面板布局、接缝、边缘、开孔，或任何部件的形状。
    不要添加任何新的细节或部件（禁止新增螺丝、铆钉、螺栓、紧固件、机械碎细节、额外通风口、额外接缝、额外面板线、贴花、标签、任何新文字）。
    严格使用参考图的构图：<一句话描述画面主体与环境>。
    保持相同的机位角度、相同的取景、相同的透视关系。
    ```
    **英文等价（负面词段）**：
    ```
    Re-shading / material upgrade only. Do NOT change geometry, silhouette, proportions, pose, armor paneling, panel layout, seams, edges, or openings.
    NO new details or parts (NO screws, NO rivets, NO bolts, NO fasteners, NO greebles, NO kitbash, NO extra vents, NO extra seams, NO extra panel lines, NO decals, NO labels, NO new text).
    Use the reference image composition exactly: <subject + environment>. Same camera angle, same framing, same perspective.
    ```
    > 用法：做"材质重抽/质感升级"时，约束词放最前；新建 @图N 关键帧时，把其中"物理材质"思路融进风格前缀，不必整段照抄约束。

[第二块 · PBR 七要点（升材质就写这些·都写物理不写形容词）]
    1. **清漆层 + 菲涅尔（Fresnel）**：裸铁几乎不反光；金属"质感"来自**斜看清漆层产生的菲涅尔反射——越斜越容易反光**。写法：`喷涂金属装甲带清漆层（真实 clearcoat 反射、准确的菲涅尔效果）`。
    2. **粗糙度变化（roughness variation）**：粗糙度**不是**"摸起来扎不扎手"，而是**表面反光是锐利还是发散**。大型机械不可能处处一样——有的面板新、有的旧、有的积灰、有的常擦 → 面板与面板之间粗糙度有差异。写法：`在现有面板上做符合物理逻辑的粗糙度变化（不均匀·面板间有差异），绝不新增几何`。
    3. **微观表面纹理**：只做**肉眼不一定注意、摄影机凑近才有**的小纹理——非常轻微的橘皮漆质感、细小微划痕、淡淡擦拭痕迹。**不是**大划痕大战损。
    4. **有逻辑的污垢/磨损**：污垢/灰尘只存在于**现有缝隙和关节内部**；边缘磨损只沿**现有边缘**出现。不凭空创造新的损坏图案。
    5. **AO（环境遮蔽）**：两结构贴得很近的地方、凹进去的夹角，因为光不容易进去会更暗。写法：`加强现有缝隙的环境遮蔽（AO）和接触阴影`。
    6. **GI（全局光照）**：GI 不是"灯照到哪亮哪"，而是光打到物体后还在环境里反弹，让整个空间的光关系更真实。写法：`改善全局光照（GI）`。
    7. **高光滚降（highlight roll-off）+ 电影调色**：高光从亮到不亮的过渡是否自然。**没有滚降 = 塑料反光、数码味重**；**有滚降 = 亮度更柔和、像电影摄影机拍的**。配合：电影调色没有绝对的黑和白，**暗部亮部都要保留信息细节**（类 ACES 色调映射）。再加极细微胶片颗粒 + 极轻微晕光（halation），**不要风格化**。

[第三块 · 可直接复制的"材质升级"提示词模板（中文）]
    ```
    仅通过 PBR 材质升级来实现：
    喷涂金属装甲，带清漆层（真实 clearcoat 反射、准确的菲涅尔效果 Fresnel）；
    在现有面板上做符合物理逻辑的粗糙度变化（不均匀、面板间有差异），绝不新增几何结构；
    仅限微观表面纹理（非常轻微的橘皮漆质感、细小微划痕、淡淡擦拭痕迹）；
    污垢/灰尘仅存在于现有缝隙和关节内部，边缘磨损仅沿现有边缘出现；
    加强现有缝隙中的环境遮蔽（AO）和接触阴影；
    改善全局光照（GI）和更真实的高光滚降（电影化 HDR / 类 ACES 色调映射）；
    细微胶片颗粒、极轻微晕光（halation），不要风格化。
    整体：更厚重、更真实的工业重量感；保持干净利落的几何设计；不做任何重新设计。
    ```
    **英文等价**：`PBR material upgrade only: painted metal armor with clearcoat (accurate clearcoat reflection & Fresnel); physically-logical roughness variation across existing panels (uneven, panel-to-panel difference), NO new geometry; micro surface texture only (subtle orange-peel, fine micro-scratches, faint wipe marks); grime/dust only in existing crevices & joints, edge wear only along existing edges; stronger ambient occlusion (AO) & contact shadows in existing seams; improved global illumination (GI) and realistic highlight roll-off (cinematic HDR / ACES-like tonemapping); fine film grain & very subtle halation, not stylized. Goal: heavier, more believable industrial weight; keep clean geometry; no redesign.`

[落到 @图N 关键帧（分镜师怎么用）]
    分镜师渲染 @图N 关键帧时：
    - **风格前缀**：把"金属 PBR 质感 + 高光滚降 + 电影 HDR"并进项目风格前缀（与 bible 登记的那条不冲突，作为质感补充）。
    - **机甲/机械/硬表面镜**：在 @图N 的「光影/质感」描述里写清菲涅尔反光、粗糙度差异、AO 缝隙、微纹理——烧进关键帧的材质质感，喂导演 production 的 i2v 当首帧。
    - **avoid**：`avoid plastic look, avoid over-clean CG, avoid clipped highlights, avoid random heavy scratches, avoid new panel lines/screws`。
    - **配合生图顺序**：质感是三道洗的第一道（精修层）——先在信息版底锁好机甲的几何/分块/构图，内容稳定后再叠材质（见 storyboard-skill 生图顺序纪律）。

[与其他 skill 的关系]
    - `cinematic-lighting-skill`：材质负责"像不像真的"，光影负责"有没有戏"。两者配合出电影级机甲：先 PBR 把表面做真，再用硬侧顶光/体积光把戏剧性打出来。
    - `art-design-skill`：风格前缀块的归属与登记（bible 同一条）；本 skill 是其"材质物理层"的补充。
    - `cinematography-skill`：镜头语言/景别/构图（材质不碰这些）。

> Copyright (c) 2026 阿泽。依据仓库根目录 LICENSE（MIT）使用。

# 视觉风格预设库

> 本文件为初始化"视觉风格"选项提供**具体提示词**。选了风格后不再只是三个字——每个预设都有压缩前缀（每张参考图必带）和完整版（参考定制用）。
>
> **专业版用途（重要）**：这些"压缩前缀"是**风格前缀块**的来源。专业版链路：服化道出身份级底 → 分镜师渲染 @图N 精修关键帧（生图·必带风格前缀）→ 喂导演 production 的 i2v 当首帧/参考 → i2v 生成视频。**服化道**把压缩前缀写进每张身份级底提示词的顶部，**分镜师**把同一条压缩前缀写进每张 @图N 关键帧提示词的顶部——两处用 bible 登记的同一条风格前缀，烧进画面。
>
> **跨风格使用**：预设不是互斥的项目级选择。真人写实项目拍空镜/大场景时可叠「3A游戏CG」提升质感；漫剧项目的环境背景也可用。按场景灵活组合。
>
> **没有合适的预设？** 见本文件末尾「风格生成器」——给出风格结构 + 网络参考，现写一个新预设存档复用。

---

## 0. 真人写实（实拍级）

**一句话**：真实摄影机实拍质感——电影感、自然光、胶片颗粒，"就是拍出来的"。

**适用**：写实题材、剧情/文艺、需要照片级真实的项目。默认风格。

### 压缩前缀

**人物：**
```
photorealistic cinematic portrait, shot on ARRI ALEXA, prime lens, natural motivated lighting, true-to-life skin texture with subsurface detail, film grain, shallow depth of field, color-graded cinematic look.
```

**场景：**
```
photorealistic cinematic environment, shot on ARRI ALEXA, anamorphic lens, natural light with practical sources, atmospheric depth, film grain, restrained color grading, true-to-life material textures.
```

> 具体机型/镜头/调色师/画幅/色温由项目在初始化时确定，并登记于 cinematography-bible（如本项目可能用 ARRI ALEXA 65 · Roger Deakins 欠曝美学 · 低饱和冷调等）。上面为通用基线，按项目替换。

---

## 1. 3A游戏CG渲染（UE5 级）

**一句话**：虚幻引擎 5 级超写实渲染，介于真人和 CG 之间的"超级真实"质感。

**适用**：大场景空镜、环境展示、科幻/奇幻世界观、建筑/城市鸟瞰、需要"比真实更好看"的任何场景。可叠加在真人写实或漫画项目的环境镜头上。

### 压缩前缀

**环境/景观：**
```
3A game CG rendering, Unreal Engine 5 visual fidelity, cinematic volumetric lighting, HDR imaging, sharp hyper-detailed textures, clean vibrant saturated colors, atmospheric perspective, clear directional light with long shadows.
```

**人物：**
```
3A game CG character rendering, Unreal Engine 5 visual fidelity, subsurface skin scattering, detailed hair strands with translucent highlights, fabric micro-texture visible, cinematic rim lighting, HDR, clean sharp focus.
```

### 完整版（按场景类型）

**A. 日光景观（用户原版优化）**
```
3A game CG rendered landscape, Unreal Engine 5 level visual quality, cinematic light and shadow, extremely rich and realistic details. Bright and clear overall image, sufficient to slightly high exposure, clean transparent colors with natural high saturation. Clear transparent sky, pure blue, soft volumetric clouds with distinct layering. Clear directional sunlight creating strong light-shadow contrast and long shadows, visible volumetric god rays enhancing spatial depth. Ground with moderate specular reflections and highlight points enhancing texture without excessive wetness. Obvious atmospheric perspective in distant views with clear depth layers. HDR imaging — highlights transparent without clipping, shadows clean without graying. Overall slight bloom glow effect, image sharp and crisp, realistic with premium game-engine visual quality.
```

**B. 夜景/霓虹**
```
3A game CG rendered night scene, Unreal Engine 5 visual fidelity, cinematic noir atmosphere. Dense volumetric fog with visible light shafts from street lamps and neon signs. Neon reflections on wet surfaces — cyan, magenta, amber — creating color separation in puddles and glass. Deep shadows with subtle bounce light preserving detail. Practical light sources only — no ambient fill. Lumen global illumination with emissive materials casting realistic color bleed. HDR imaging with controlled bloom on light sources, deep blacks without crushing. Sharp foreground, atmospheric depth haze in background. Cinematic color grading with teal-orange split toning.
```

**C. 室内/建筑**
```
3A game CG rendered interior, Unreal Engine 5 visual fidelity, architectural visualization quality. Single dominant light source through window creating strong directional shadows across surfaces. Visible dust particles in light beams. Realistic PBR materials — wood grain, marble veining, fabric weave, metal brushed texture all clearly distinguishable. Subtle ambient occlusion in corners and crevices. HDR imaging with bright window not clipping, shadow areas retaining color and detail. Lumen indirect illumination providing natural color bounce from walls. Clean sharp textures, shallow depth of field on foreground objects.
```

**D. 人物特写**
```
3A game CG character close-up, Unreal Engine 5 rendering quality. Subsurface scattering on skin — translucent ear tips, subtle vein visibility on temples. Individual hair strands with specular highlights and translucency against backlight. Iris detail with caustic light refraction. Micro-texture on skin pores visible but not exaggerated. Fabric material distinction clear — cotton weave vs leather grain vs metal buckle. Cinematic three-quarter rim lighting with soft fill. HDR, clean bokeh background, razor sharp on eyes. Photorealistic but with that unmistakable "better than real" CG polish.
```

**E. 动作/战斗**
```
3A game CG action scene, Unreal Engine 5 visual fidelity, dynamic cinematic composition. Motion blur on fast-moving elements only — environment stays sharp. Particle effects — sparks, debris, energy trails — with volumetric light interaction. Dramatic low-angle or Dutch angle composition. High contrast directional lighting with deep shadows. HDR with controlled highlight bloom on explosions and energy effects. Atmospheric dust and haze adding depth layers. Sharp focus on character's face/eyes even in motion. Cinematic slow-motion quality — every detail frozen in hyper-clarity.
```

---

## 2. 皮克斯风格（Pixar 3D）

**一句话**：圆润、温暖、表情夸张的 3D 动画，角色让人一眼就想亲近。

**适用**：面向全年龄的温情故事、家庭/儿童题材、喜剧、需要角色亲和力的项目。

### 压缩前缀

**角色：**
```
Pixar 3D animation style, soft rounded character design, oversized expressive eyes, warm cinematic lighting, smooth subsurface skin shading, vibrant saturated color palette, shallow depth of field, emotional facial expression.
```

**场景：**
```
Pixar 3D animation style environment, warm golden hour lighting, rich saturated colors, soft ambient occlusion, detailed miniature-like textures, inviting atmosphere, gentle volumetric haze, cinematic depth of field.
```

### 完整版

**角色完整版：**
```
Pixar-quality 3D animated character, smooth rounded proportions with slightly oversized head. Large expressive eyes with detailed iris reflections and subtle moisture. Soft subsurface scattering on skin with warm undertones. Smooth rounded features — no sharp edges. Hair rendered as soft volumetric mass with subtle strand highlights. Clothing with simplified but readable fabric texture. Warm three-point cinematic lighting — key light golden, fill light cool blue, rim light subtle. Rich saturated color palette reflecting character personality. Soft shadow edges. Clean background with shallow depth of field bokeh. Expression conveying clear readable emotion — eyes doing most of the storytelling.
```

**场景完整版：**
```
Pixar-quality 3D animated environment, warm inviting atmosphere. Rich saturated colors with intentional palette — warm tones for safe spaces, cool tones for unknown territory. Soft global illumination with gentle shadows — no harsh contrast. Detailed textures that read as charming rather than photorealistic — slightly stylized wood grain, painted-look surfaces, rounded geometry on all objects. Miniature model quality — everything slightly rounder and cuter than real life. Volumetric atmospheric haze for depth. Practical light sources (lamps, windows, candles) providing warm motivated lighting. Background elements slightly softer and less detailed than foreground, creating natural focus. Every prop tells a story about who lives in this space.
```

---

## 3. 迪士尼风格（Disney 3D）

**一句话**：比皮克斯更"魔法感"——更强的光效、更梦幻的色彩、更戏剧化的构图。

**适用**：奇幻/童话题材、公主/英雄叙事、需要"壮丽+温暖"并存的视觉、音乐剧类项目。

### 压缩前缀

```
Disney 3D animation style, magical cinematic lighting with visible light rays, dramatic color palette with warm-cool contrast, expressive character animation, detailed hair dynamics, enchanted atmosphere with subtle sparkle particles, epic wide-angle compositions.
```

### 完整版

```
Disney-quality 3D animation, cinematic grandeur with emotional intimacy. Characters with expressive stylized proportions — large eyes with complex light refraction, detailed flowing hair with physics-driven movement. Dramatic motivated lighting — golden magic-hour key light, deep blue shadow fill, ethereal rim glow. Color palette shifts with emotional beats — warm golds for hope, deep blues for mystery, vivid greens for nature magic, rich purples for villainy. Visible volumetric light rays through forest canopy or castle windows. Subtle particle effects — floating dust motes, magical sparkles, firefly-like ambient lights. Epic landscape compositions with dramatic scale contrast (small character vs vast world). Rich environmental storytelling — every background element contributing to world-building. Fabric simulation on flowing capes and dresses. Water and ice rendered with prismatic light refraction. Overall feeling: magical realism — grounded enough to believe, beautiful enough to dream.
```

---

## 4. 国漫风格

**一句话**：东方美学 + 现代渲染技术——水墨意境与 CG 精度并存。

**适用**：仙侠/玄幻题材、武侠、中国历史/神话、需要东方审美但不是日漫的项目。

### 压缩前缀

**仙侠/玄幻：**
```
Chinese animation style (guoman), ink wash painting influence with modern 3D CG rendering. Flowing brush-stroke energy effects, traditional Chinese architectural details, ethereal cloud and mist atmosphere, jade-toned color palette with gold accents, dynamic martial arts poses, silk and ribbon physics.
```

**都市/现代：**
```
Modern Chinese animation style (guoman), clean line art with soft cel-shading, contemporary urban Chinese setting, warm natural lighting, realistic proportions with slightly stylized features, muted earth-tone palette with selective vivid accents, slice-of-life atmospheric detail.
```

### 完整版（仙侠/玄幻）

```
Chinese fantasy animation (仙侠国漫) visual style. Fusion of traditional ink wash painting aesthetics with modern 3D CG rendering precision. Characters with elegant East Asian features — sharp jawline, narrow eyes with intense gaze, flowing long hair with physics-driven movement. Traditional Chinese costume detail — layered robes (汉服), jade ornaments, intricate embroidery patterns visible. Energy/magic effects rendered as flowing calligraphic brush strokes — chi energy as luminous ink trails. Environment: traditional Chinese architecture (飞檐斗拱) with dramatic mountain-and-cloud backdrops, volumetric mist between peaks creating ink-wash depth layers. Color palette: jade green, celestial gold, ink black, cinnabar red — with desaturated backgrounds pushing saturated foreground characters. Lighting: dramatic directional light from above (天光) with ethereal rim glow on characters. Silk ribbons and fabric with exaggerated flowing physics. Martial arts action with dynamic speed lines and impact energy bursts. Overall: the precision of CG with the soul of Chinese painting.
```

---

## 5. 日漫风格（三个子类）

### 5a. 新海诚风格

**一句话**：现实场景 + 超高饱和光影 + 情绪化天空——"比照片更美的现实"。

**压缩前缀：**
```
Makoto Shinkai anime style, hyper-detailed realistic backgrounds with stylized characters, ultra-vivid saturated sky with dramatic cloud formations, golden hour lens flare, rain and light particle effects, emotional atmospheric lighting, sharp architectural detail, reflective wet surfaces.
```

**完整版：**
```
Makoto Shinkai (新海诚) visual style. Photorealistic background environments with extraordinary color saturation and lighting — real-world locations rendered more beautiful than reality. Sky as emotional canvas — towering cumulus clouds with internal golden light, gradient from deep blue to warm amber, visible crepuscular rays. Urban environments with obsessive architectural detail — every window, wire, and signboard rendered. Wet surfaces reflecting sky colors. Characters in simplified anime style contrasting with hyper-detailed backgrounds. Lens effects: natural lens flare from sun, chromatic aberration at frame edges, shallow depth of field with circular bokeh. Rain/snow particles catching light individually. Interior scenes with dust motes in window light beams. Color grading: push saturation beyond reality — blues bluer, golds warmer, greens more vivid. Every frame composition suitable for desktop wallpaper. Emotional tone conveyed entirely through lighting and weather — sunshine = hope, rain = melancholy, twilight = nostalgia.
```

### 5b. 赛璐璞 TV 动画

**一句话**：经典日本动画的平涂色块 + 清晰描边——干净、高效、标志性。

**压缩前缀：**
```
Japanese cel-shaded anime style, clean black outlines, flat color fills with hard-edge shadow cuts, limited color palette per character, bright even lighting, minimal background detail, expressive simplified facial features, TV anime production quality.
```

### 5c. 厚涂电影动画（Arcane 级）

**一句话**：每一帧都是油画——笔触可见、色彩厚重、电影级光影。

**压缩前缀：**
```
Arcane/Fortiche thick-paint 3D CG animation style, visible brush stroke textures on surfaces, rich painterly color with medium saturation, dramatic cinematic chiaroscuro lighting, detailed character expressions with realistic proportions, layered atmospheric depth, oil-painting-like color blending on skin and environments.
```

---

## 6. 韩漫/Webtoon 风格

**一句话**：竖屏长条漫画美学——柔和渐变、精致五官、梦幻光效。

**适用**：竖屏短剧、恋爱/都市题材、需要"精致美型"角色的项目。05-竖屏版首选。

### 压缩前缀

```
Korean webtoon (manhwa) art style, soft gradient shading without hard shadow edges, beautiful detailed character faces with refined features, luminous skin with soft highlight bloom, pastel color palette with selective vivid accents, clean minimal backgrounds with soft focus, romantic atmospheric lighting, vertical composition optimized.
```

### 完整版

```
Korean webtoon (manhwa) visual style optimized for vertical scroll format. Characters with refined beautiful features — detailed eyes with multiple light reflections, small nose and lips with soft shading, smooth luminous skin with subtle blush. Soft gradient cel-shading — NO hard shadow cuts (unlike Japanese anime). Hair rendered with individual strand highlights and soft color gradients. Color palette: soft pastels (lavender, rose, mint) as base with selective vivid accent colors for emotional moments. Backgrounds simplified and soft-focused — watercolor-wash style environments that don't compete with character focus. Lighting: dreamy diffused light with soft bloom on highlights, backlight creating hair glow halo. Emotional color coding — warm pink tones for romance, cool blue for melancholy, golden for nostalgia. Panel composition optimized for vertical scroll — dramatic vertical reveals, close-up to wide-shot transitions within single scroll. Minimal speed lines — emotion conveyed through color shift and lighting change rather than motion effects.
```

---

## 7. 爱死机风格（Love, Death & Robots 级 CG）

**一句话**：跟 3A游戏CG 同级渲染精度，但更暗、更粗粝、更成人向——工业质感 + 电影 noir 光影。

**适用**：成人向科幻/恐怖/赛博朋克、暴力美学、需要"不舒服的真实感"的项目。与 3A游戏CG 的区别：3A 是"比真实更好看"，爱死机是"比真实更脏更疼"。

### 压缩前缀

**通用：**
```
Love Death and Robots CG style, photorealistic rendering with gritty industrial texture, cinematic noir lighting with deep shadows, desaturated color palette with selective vivid accent, visible surface wear and micro-damage, subsurface skin scattering with sweat and dirt, atmospheric haze, anamorphic lens.
```

### 完整版（按场景类型）

**A. 角色/对峙**
```
Love Death and Robots photorealistic CG character rendering. Skin with pore-level detail — visible sweat droplets, minor scars, sunburn texture, dirt in creases. Subsurface scattering showing blood under skin at thin areas (ears, nostrils, fingers against light). Eyes with bloodshot detail and moisture film. Hair individually rendered but greasy, matted, or wind-damaged — not salon-perfect. Clothing with visible wear — frayed edges, faded patches, stretched seams, accumulated dust. Hard directional key light with minimal fill — deep noir shadows hiding 40-60% of face. Practical light sources only (fire, screen glow, emergency red). Desaturated base palette with one vivid accent color per scene (arterial red, electric blue, toxic green). Anamorphic lens characteristics — horizontal flare, oval bokeh, slight barrel distortion. Shallow depth of field isolating subject against dark atmospheric background. Overall: photorealism pushed past beauty into uncomfortable intimacy.
```

**B. 环境/废墟**
```
Love Death and Robots CG environment. Industrial post-apocalyptic or dystopian setting with obsessive surface detail — rust patterns, concrete spalling, peeling paint layers, biological growth on metal. Volumetric atmospheric haze with visible particulate — dust, smoke, spores. Lighting from practical sources only — flickering fluorescent tubes, distant fire, bioluminescent organisms, screen glow. Deep shadows with subtle colored bounce light from environment (green from moss, orange from rust, blue from screens). Wet surfaces with oil-rainbow-sheen puddles reflecting fragmented light. Cables, pipes, and infrastructure exposed — nothing is clean or maintained. HDR with extreme contrast — bright light sources blooming, deep blacks preserving just enough detail. Sense of scale communicated through environmental decay — small human elements against vast broken machinery. Color grading: teal shadows, amber highlights, crushed mid-tones.
```

**C. 动作/暴力美学**
```
Love Death and Robots CG action sequence. Hyper-detailed violence rendered with clinical precision — physics-accurate material destruction, fluid dynamics on liquids. Extreme slow-motion freeze-frame quality — every particle, shard, and droplet individually lit and in focus. Dramatic camera angles — extreme low angle, over-the-shoulder tight, overhead God's-eye view. Single dominant light source creating theatrical shadow play during action. Motion blur only on fastest elements — environment razor sharp. Particle interaction with volumetric light — sparks casting moving shadows, muzzle flash illuminating faces for single frames. Desaturated environment with hyper-saturated action elements (vivid red on grey). Anamorphic lens distortion amplifying speed and impact. Sound-design-driven visual rhythm — impacts timed with compositional emphasis.
```

---

## 8. EVA CG（新世纪福音战士·CG 重制）

**一句话**：EVA 的设计 DNA（初号机紫绿黑 + 琥珀内构 + 独角单目 + 约束装甲 + 末世宗教母题），用现代电影级 3DCG"拍"出来——不是赛璐璐手绘，是硬表面清漆 + 半透内构 + 机库荧光 + 体积烟尘的渲染质感。

**适用**：EVA 风格重型人形机甲、末世废墟巨物对决、NERV 工业机库/发射台、宗教崇高感的机甲题材。**与"日漫·赛璐璐 TV 动画"(§5b) 的区别**：那是平涂硬边手绘，这是带物理光影的 CG 渲染。此预设仅在用户选择相应视觉方向时启用。

**参考素材**：公开版不包含图片示例。请使用自有或获得授权的参考图；缺少参考时跳过图片读取。

> ⚠️ **风格 vs 身份分工**：本前缀只管"怎么渲染"（CG 质感/配色/光影/母题）。具体机体的造型身份（独角形状、分块、配色分布、做旧）由该机甲的 identity 卡 + 用户提供的参考图 承载——服化道写身份级底时**只写身份 delta，不堆通用渲染物理词**（clearcoat/Fresnel/AO 那套归分镜师第一道洗）。本前缀作为顶部风格锚登记，分镜师渲染 @图N 关键帧时落地质感。

### 压缩前缀

**人物/机甲：**
```
Neon Genesis Evangelion reimagined as cinematic 3DCG, biomechanical humanoid EVA-type mecha with restraint armor plating, single horn and glowing slit eyes, royal purple with fluorescent green and black and amber translucent internals. Hard-surface clearcoat metal with Fresnel edge sheen and panel-to-panel roughness variation, amber subsurface-scattering inner glass, weathered scratches and grime in seams, cinematic HDR highlight roll-off, fine film grain. Desaturated cold blue-grey base with blood-red and purple-green and amber accents, dramatic hard rim lighting, volumetric haze.
```

**场景/环境：**
```
Neon Genesis Evangelion cinematic 3DCG environment, NERV industrial brutalist architecture with yellow-black hazard stripes, green fluorescent tube lighting and emergency red accents, anamorphic blue lens flare, exposed cables pipes and restraint cages, volumetric atmospheric haze and dust, desaturated cold blue-grey and charcoal palette with purple-green and amber glow, religious geometric symbolism, apocalyptic monumental scale, fine film grain.
```

### 完整版（按场景类型）


```
Cinematic 3DCG hero render of an EVA-type humanoid mecha, full body battle stance. Extreme low-angle framing emphasizing monumental scale. Hard-surface clearcoat armor — royal purple plating with fluorescent green segments and black bodysuit, amber translucent resin at joints. Accurate Fresnel edge sheen, panel-to-panel roughness variation, micro-scratches and combat grime in seams, deep ambient occlusion in armor gaps. Dramatic hard key light from one side with strong rim light separating the mecha from a hazy desaturated battlefield of rubble and broken skyscrapers. Volumetric dust and floating debris particles catching light. Cold blue-grey atmosphere with one blood-red or amber accent. Cinematic HDR highlight roll-off, anamorphic shallow depth of field, fine film grain. Photoreal CG fidelity, not cel animation.
```


```
Cinematic 3DCG NERV launch-cage interior, an EVA-type mecha suspended in industrial restraint arms. Cavernous brutalist hangar with exposed structural beams, yellow-black hazard chevron stripes, banks of green-white fluorescent tubes overhead, emergency red panel lights. Strong anamorphic horizontal blue lens flare across frame. Wet industrial surfaces with subtle reflections, volumetric haze filling the deep space, god-ray shafts from overhead lights through dust. The mecha's amber inner glass glows faintly, clearcoat armor catching cold rim light. Desaturated teal-grey palette with green and amber accents and warning-red pops. Wide cinematic 2.39:1 composition, deep perspective, fine film grain, photoreal CG render.
```

**C. 城市废墟战斗（巨物对决·尺度奇观）**
```
Cinematic 3DCG action scene, EVA-type mecha fighting amid a destroyed Tokyo-3 cityscape. Towering skyscrapers crumbling, dust clouds and debris fields, distant smoke columns. Dynamic dramatic pose with weapon (rifle / progressive knife / Lance). High-contrast directional daylight or overcast hard light, deep shadows, atmospheric perspective into hazy ruined distance. Hard-surface clearcoat armor with realistic material weight, combat damage and scorch marks, motion-implied debris frozen mid-air. Desaturated cold palette with purple-green mecha as the saturated focal accent. Cinematic HDR, anamorphic lens characteristics, fine film grain, monumental sense of scale.
```


```
Cinematic 3DCG EVA key-art composition, painterly-photoreal hybrid. Monumental EVA-type mecha against an apocalyptic sky — blood-red sun or halo ring, towering cumulus clouds with internal god-rays, religious geometric symbolism (cruciform, AT-field hexagons, concentric halos). Single horn silhouette, glowing slit eye venting steam. Extreme scale contrast — a tiny human in a plug-suit dwarfed below. Concrete brutalist bunker or rubble foreground. Desaturated cold base with intense blood-red and purple-green and amber accents. Dramatic chiaroscuro, volumetric atmosphere, sublime melancholic religious awe. Cinematic poster framing, fine film grain. (Optional bold Japanese typographic title and blood-splatter graphic accents.)
```

**E. 头部 / 内构特写（质感名片）**
```
Cinematic 3DCG extreme close-up of an EVA-type mecha head and shoulders. Hard-surface clearcoat helmet armor with razor-sharp panel lines, single horn, glowing green or red slit eye. Visible amber translucent resin internals with subsurface scattering between armor plates — like backlit glass and resin. Accurate clearcoat Fresnel reflections, roughness variation between matte and gloss panels, deep ambient occlusion in seams, fine micro-scratches and dust. Cold rim light raking across the surface, one warm amber internal glow. Shallow depth of field, anamorphic bokeh, cinematic HDR highlight roll-off, fine film grain. Photoreal CG material believability, not cel shading.
```

### 生图 avoid（EVA 专属·接在通用 avoid 后）
```
avoid cel-shaded flat anime look, avoid plastic toy / clean glossy showroom CG model feel, avoid flat unmotivated fill light, avoid oversaturated cartoon colors, avoid text overlays / HUD elements / watermark, avoid extra fingers / deformed hands.
```

---

## 9. 凡人修仙传（3D 动画版·原力国风仙侠写实 CG）

**一句话**：原力动画版《凡人修仙传》的写实路线——真人动捕级写实角色（精细微表情、贴近真人五官、**不是 3D 网红脸/平涂日漫脸**）+ UE5 Lumen 电影级光追 + 实物扫描质感环境，套上"国风仙侠美学体系"（简约留白、水墨东方意境），把修仙世界"拍"成近真人剧的写实 CG；**大远景/夜景再叠一层灵气玄幻 epic 氛围**——灵气星河绕青山、弦月星空、雾谷灯火、画意 photoreal 的尺度奇观（融自"灵气青山"参照）。

**适用**：凡人修仙传二创、写实国风仙侠/玄幻修真、宗门洞府秘境、御剑斗法、法宝丹药符箓、大漠灵山的修真世界题材。**与"国漫"(§4)、"日漫"(§5) 的区别**：那些是手绘/平涂/动画脸，这是 UE5 真人动捕级写实 CG（电影级光追 + 实物扫描环境 + 微表情）。

**参考素材**：图片示例不随仓库分发，请用户自行提供有权使用的参考。



> **两层融合是本包的核心**：角色/中近景走原力写实CG（真人五官·实物扫描质感），大远景/夜景叠一层灵气玄幻 epic 氛围（灵气星河·星空·留白意境）。

> ⚠️ **风格 vs 身份分工**：本前缀只管"怎么渲染"（写实 CG 质感/国风光影/灵气特效母题）。具体角色的造型身份（韩立的朴素青年修士相、特定法袍、特定法宝外形）由该角色的 identity 卡 + 垫图承载——服化道写身份级底时**只写身份 delta，不堆通用渲染物理词**（SSS/Lumen/粒子那套归分镜师渲染落地）。本前缀作为顶部风格锚登记，分镜师渲染 @图N 关键帧时落地质感。

### 压缩前缀

**人物：**
```
Chinese xianxia cultivation 3DCG in the photoreal style of donghua "A Record of a Mortal's Journey to Immortality", UE5 Lumen cinematic rendering, motion-capture-grade realistic human face with fine micro-expressions, natural skin subsurface scattering and pore detail, grounded real-person facial proportions (NOT stylized anime or "internet-celebrity" 3D face), restrained Daoist cultivator robes with naturally flowing fabric, minimalist elegant guofeng design, subtle drifting spirit-qi and spell particle effects, desaturated natural ink-wash palette with selective jade-green / spirit-light accents, soft volumetric atmosphere, cinematic depth of field, fine film grain, photoreal CG not cel animation.
```

**场景：**
```
Chinese xianxia cultivation world 3DCG environment, photoreal donghua "Mortal Journey" style, UE5 Lumen global illumination with ray-traced light, photoscanned-realistic oriental architecture and nature (sect halls and pavilions, grotto-heaven caves, spirit mountains, desert wastes, market towns, ancient ruins), minimalist negative-space guofeng composition rooted in ink-wash painting, drifting spiritual qi mist and floating spirit motes, naturalistic cinematic lighting (golden-hour exteriors, softly glowing cave interiors lit by spirit stones), desaturated jade-green / ink-grey / earth-tone palette with luminous spirit-light accents, volumetric god-rays and haze, fine film grain, photoreal CG fidelity.
```

### 完整版（按场景类型）

**A. 角色 / 文戏对峙** — 写实修士面孔·内敛克制
```
Photoreal donghua-style 3DCG character render of a Chinese cultivator, "Mortal Journey" realism. Motion-capture-grade face with subtle micro-expressions — slight brow tension, restrained eyes, natural skin with pores, faint sweat sheen and subsurface scattering, grounded real-person proportions, absolutely not anime or internet-celebrity stylization. Daoist robe / cultivator garb in muted natural dyes with naturally draping fabric, jade pendant or storage-pouch details. Soft cinematic key light with gentle fill, UE5 Lumen bounce, shallow depth of field isolating the face against a hazy oriental backdrop. Desaturated ink-wash palette, one quiet jade-green or spirit accent. Volumetric atmosphere, fine film grain, photoreal CG.
```

**B. 御剑飞行 / 斗法** — 飞剑剑光·法术粒子
```
Photoreal donghua-style 3DCG cultivation battle, "Mortal Journey" realism. A cultivator commanding flying swords / magic treasures mid-air, jade-green sword-qi light trails and ray-traced glowing spell effects, swirling qi particles and igniting talisman runes. Dynamic but grounded motion (real-person action-director feel, not exaggerated anime), cinematic motion blur on the fastest elements only. Dramatic UE5 Lumen lighting with the spell-light as a key practical source casting moving colored shadows. Desaturated environment with hyper-saturated spirit-light accents (jade-green, azure, crimson danger). Volumetric haze catching the magic glow, deep cinematic perspective, fine film grain, photoreal CG.
```

**C. 洞府 / 秘境 / 宗门内景** — 灵石辉光·阵法
```
Photoreal donghua-style 3DCG cultivation interior, "Mortal Journey" realism. A grotto-heaven cave dwelling or sect hall — carved stone, wooden beams, an alchemy furnace, formation arrays etched into the floor glowing faintly. Soft spirit-stone light and glowing formation runes as practical sources, UE5 Lumen ray-traced bounce, god-ray shafts through drifting qi mist. Photoscanned-realistic surface detail on stone, wood and bronze ritual objects. Desaturated jade-grey palette with warm lantern and cool spirit-light accents. Minimalist guofeng composition with negative space, volumetric atmosphere, fine film grain, photoreal CG depth.
```

**D. 大漠 / 灵山 / 外景奇观** — 尺度·黄昏·东方山水
```
Photoreal donghua-style 3DCG cultivation landscape, "Mortal Journey" realism. Vast oriental wilderness — spirit mountains shrouded in a cloud-sea, endless desert wastes (Land of Chaotic Stars), ancient ruined battlefields, floating peaks. Golden-hour or overcast cinematic light, UE5 Lumen ray-traced atmosphere with deep aerial perspective into haze. A tiny lone cultivator dwarfed by monumental natural scale, ink-wash negative-space composition. Desaturated earth and jade tones, distant spirit-light glow. Drifting clouds and spirit mist, volumetric god-rays, fine film grain, photoreal CG, sublime oriental landscape mood.
```

**E. 法宝 / 丹药 / 符箓特写** — 质感名片
```
Photoreal donghua-style 3DCG extreme close-up of a magic treasure, "Mortal Journey" realism. A flying sword / spirit flag / jade vial / glowing talisman / alchemy pill, photoscanned-grade material believability — aged bronze patina, jade translucency with subsurface scattering, lacquered wood grain, paper-talisman fibers with glowing vermilion runes. Spirit-qi energy faintly flowing across the surface. Shallow macro depth of field, UE5 Lumen reflections and roughness variation, cold ambient with one warm spirit-glow. Volumetric particle motes, fine film grain, photoreal CG, not cel shading.
```

**F. 灵气玄幻 epic 夜景 / 星河大远景** — 画意photoreal·氛围尺度（融自"灵气青山"参照）
```
Epic cinematic xianxia night vista, painterly-photoreal "Mortal Journey" mood. Vast misty jade-green mountains under a deep blue star-filled night sky with a crescent moon. A luminous flowing river of blue-cyan spirit-qi energy winding and coiling through the peaks like a celestial ribbon, glittering with particle light. Warm amber town lights glowing through low valley mist far below, traditional Chinese pavilions and arched bridges silhouetted in the foreground. A tiny lone robed Daoist cultivator dwarfed against the monumental scale, ink-wash negative-space composition. Deep teal-blue palette with glowing jade-cyan spirit-light and warm amber accents, volumetric god-rays and drifting mist, painterly-photoreal cinematic concept-art fidelity, fine film grain, sublime oriental fantasy awe.
```

### 生图 avoid（凡人专属·接在通用 avoid 后）
```
avoid cel-shaded flat anime look, avoid stylized anime / "internet-celebrity" 3D face, avoid oversaturated gaudy xuanhuan colors, avoid generic western fantasy aesthetic, avoid plastic toy CG feel, avoid flat unmotivated lighting, avoid text overlays / HUD / watermark, avoid extra fingers / deformed hands.
```

---

## 使用说明

### 谁用 · 何时用 · 用在哪（专业版核心）
- **谁**：服化道（art-designer）写身份级底时；分镜师（director）渲染 @图N 关键帧时。
- **何时**：生图阶段——写人物/场景**身份级底提示词**时，以及写 **@图N 关键帧提示词**时。
- **用在哪**：把压缩前缀放在每张身份级底提示词、以及每张 @图N 关键帧提示词的**最顶部**，作为"风格前缀块"的第一部分（第二部分是生图 avoid）。两处写 bible 登记的同一条压缩前缀。
- **注意**：风格前缀服务生图（身份级底 + @图N 关键帧）；导演 production 的 i2v 视频提示词另写运镜/分镜动作链，不带这套生图风格前缀（i2v 靠 @图N 首帧继承画面风格）。

### 三步用法
1. **选风格**（初始化时）：用户从预设里选 → 取对应预设的**压缩前缀**（人物用人物版、场景用场景版）。预设没合适的 → 走文末「风格生成器」现写一个。
2. **登记**：把选定的压缩前缀登记进 `assets/cinematography-bible.md`，作为全片风格基线。
3. **每张参考图套用**：服化道写每张人物/场景提示词时，顶部 = 压缩前缀 + 生图 avoid（见 art-design-skill 的「风格前缀块·硬规则」）。

### 示例（人物参考图顶部）
```
photorealistic cinematic portrait, shot on ARRI ALEXA, prime lens, natural motivated lighting,
true-to-life skin texture with subsurface detail, film grain, shallow depth of field, color-graded cinematic look.
avoid text overlays, avoid HUD elements, avoid watermark, avoid extra fingers, avoid deformed hands.

<下面接中文叙事式的角色设定描述：整体定位 / 面部 / 体型 / 服装 / 配饰 / 气质……>
```

### 场景级叠加（跨风格混用）
项目基底是 A 风格，但某些场景需要 B 风格的环境质感：
- 在该场景的提示词中，**替换环境描述部分**为 B 风格的对应场景变体
- 人物部分保持 A 风格的前缀不变
- 示例：真人写实项目 + 3A游戏CG的「日光景观」变体用于空镜

### 调参建议
- 所有前缀都是**起点**——根据具体场景微调关键词权重
- 色彩饱和度、曝光、光影对比是最常需要调的参数
- 夜景和日景使用不同变体，不要用日景前缀拍夜景

---

## 风格生成器（预设没命中·按 7 维现拆一个）

> **导演/影片/流派风格优先查库**：**主源 = `cinematography-skill/styles/_风格方法论与库.md §B`（全 63 条·7 维方法论）**；`style-library.json` 是它的**机读镜像（已收录 19 条常用·部分镜像）**：库布里克/塔可夫斯基/黑泽明/林奇/黑色电影/原子朋克/赛博朋克/王家卫/新海诚/宫崎骏…。**查库优先看 MD §B**（JSON 未收的以 MD 为准）；库里有 → 直接取前缀；没有 → 按下面现拆。

用户想要的风格不在预设、也不在导演库里时，**按 7 维方法论现拆一个新风格条目**并存档复用：

**第一步 · 按 7 维拆解（向用户索取代表作/参考图，逐维提炼）**
照 `_风格方法论与库.md` 的 7 维逐维填：① 摄影机/镜头 ② 构图 ③ 光影 ④ 色彩/调色 ⑤ 质感/介质 ⑥ 氛围/母题 ⑦ 运动/节奏。
向用户索取：①一部代表作 / 导演 / 流派名 ②一张网络参考图 → 据此逐维提炼视觉特征。

**第二步 · 生成新预设条目**
仿照以上预设格式，产出：
- **一句话**定义
- **适用**场景
- **压缩前缀**（人物版 + 场景版·英文·每张参考图顶部用）
- **完整版**（可选·按场景类型）

**第三步 · 存档登记**
- **导演/影片/流派风格** → 追加进 `cinematography-skill/styles/_风格方法论与库.md` + `style-library.json`（7 维字段 + 前缀 +（如有）实例图）
- **通用美学风格** → 追加为本文件新的一节（编号顺延）
- 同步把该项目采用的压缩前缀登记到 `assets/cinematography-bible.md`
- 之后服化道的"风格前缀块"即取自此

> 风格生成器产出的前缀同样服务生图——服化道写进身份级底、分镜师写进 @图N 关键帧，两处同一条。导演 production 的 i2v 视频提示词另写运镜/分镜动作链，不带这套生图前缀。

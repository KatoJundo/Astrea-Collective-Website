# ASTREA Collective · Website V2.0

> 在既定之中，成为未定 · *Within the Given, Become the Unwritten.*

[astreacollective.com](https://astreacollective.com/) —— ASTREA Collective（泰拉星螺协会）的官方入口页。

V2.0 在 V1.0 的结构上做视觉重构：沿用「入口 → 电台 → 自我介绍卡 → 联系管理员」的顺序与折叠卡片交互，
视觉语言延续 V2 海报（蓝白版）：群青墨色、淡紫纸面、版画线稿、工程图标注（Label_0X、编号节点）、Bodoni 衬线大字与极细中文。
新增 ORIGO Minecraft 服务器、ASTREA 3.0、研究所档案三块预告。复杂功能（账号、论坛、Card 编辑）留给 3.0。

## 页面结构

| 章节 | 内容 |
| --- | --- |
| 首屏 | 星螺座标志（编号线稿）、观测仪刻度环与访客本地时间、黄金螺线「星螺座」星图、版画羽翼 |
| I · PORTA 入口 | 微信群二维码、KOOK 语音频道 |
| II · VOX 电台 | Dawn FM |
| III · FUTURA 即将到来 | 信号日志、ORIGO（三种视界可切换的体素浮岛）、ATRIUM 柱廊示意、ASTREA 3.0 平面图、ASTREA 自我介绍卡 |
| IV · ARCHIVUM 档案 | Karis / Uranus / Lucia 档案预览 |
| V · NUNTIUS 联系 | 管理员二维码、邮箱 |

右上角按钮可切换「昼 / 夜」两套配色（对应 V2 / V1 海报），选择会记在浏览器里。
页面所有装饰图形（刻度环、羽翼、拱门、浮岛、柱廊、平面图）均由 `index.html` 内的脚本用 SVG 实时绘制，没有额外图片。

## 常见维护

- **更换微信群二维码**：直接用同名文件覆盖根目录的 `群二维码.jpg`（微信群二维码每 7 天失效一次）。
- **更换管理员二维码**：覆盖 `admin.jpg`。
- **修改文字**：编辑 `index.html`。如果加入了页面上原本没有的汉字，运行一次 `python tools/subset_font.py` 重新生成中文字体子集；不运行也能显示，只是新字会退回到系统字体。

## 文件

```text
index.html                      页面（样式与脚本内联）
群二维码.jpg / admin.jpg         二维码（沿用 V1 文件名）
assets/favicon.svg              站点图标
assets/fonts/                   字体子集：Astrea Sans（阿里妈妈方圆体子集）、Bodoni Moda、IBM Plex Mono
assets/img/                     Dawn FM 封面、角色立绘、主城封面（© StarryYino）、分享图
tools/subset_font.py            重新生成中文字体子集
AlimamaFangYuanTiVF-Thin.ttf    中文字体原文件（子集的来源，网页不直接加载）
```

## 署名

- 字体：阿里妈妈方圆体（Alibaba）、Bodoni Moda（SIL OFL 1.1）、IBM Plex Mono（SIL OFL 1.1）
- ORIGO 主城基础：[ISLAND Moonlight](https://www.planetminecraft.com/project/island-moonlight-fantasy-build-download/) © StarryYino
- Minecraft © Mojang / Microsoft；《明日方舟》相关内容版权归其权利方所有。本站为非营利玩家社群，与官方无关。
- ASTREA 研究所世界观（Karis / Uranus / Lucia 等）是基于《明日方舟》世界观的二次创作，与官方正传无关，不代表官方设定。

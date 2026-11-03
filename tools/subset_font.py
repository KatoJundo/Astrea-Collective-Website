"""
重新生成网页用的中文字体子集（阿里妈妈方圆体 VF）。

什么时候需要运行：修改了 index.html 里的中文文字，发现新加的字显示成了系统字体。
用法（在仓库根目录）：
    pip install fonttools brotli
    python tools/subset_font.py
它会读取 index.html 中出现的所有字符，从 AlimamaFangYuanTiVF-Thin.ttf 生成
assets/fonts/astrea-sans.woff2（只含页面用到的字，约 150KB，而原字体 7MB）。
"""
import html, os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools import subset

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "AlimamaFangYuanTiVF-Thin.ttf")
OUT = os.path.join(ROOT, "assets", "fonts", "astrea-sans.woff2")

text = html.unescape(open(os.path.join(ROOT, "index.html"), encoding="utf-8").read())
chars = set(text) | {chr(c) for c in range(0x20, 0x7F)} | set("，。、：；！？「」『』（）《》—…·“”‘’　")

font = TTFont(SRC)
if "STAT" in font:
    del font["STAT"]
font = instancer.instantiateVariableFont(font, {"BEVL": 1, "wght": (200, 500)})
opt = subset.Options()
opt.flavor = "woff2"
opt.layout_features = ["*"]
sub = subset.Subsetter(opt)
sub.populate(text="".join(sorted(chars)))
sub.subset(font)
font.flavor = "woff2"
font.save(OUT)
print("wrote", OUT, os.path.getsize(OUT) // 1024, "KB")

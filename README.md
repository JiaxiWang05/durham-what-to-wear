# durham-what-to-wear

根据杜伦 (Durham, UK) 当天天气，从自己的衣服库里推荐穿搭，并把衣服拼在一起预览。页面右上角可切换 English / 中文。

Outfit picks from your own wardrobe for today's weather in Durham, UK, with a flat-lay preview. Toggle English / 中文 at the top right.

- 打开 / Open: https://jiaxiwang05.github.io/durham-what-to-wear/
- 天气来自 [Open-Meteo](https://open-meteo.com/)（免费，无需 key），按白天 08–20 点体感温度和降水概率推荐
- **日常 / Go out ✨**：Go out 只选可爱款，里面按室内 15–22°C 搭配，外套按真实天气、优先可爱款
- 天气主要决定外套：穿外套时里面厚薄都可以，所以上衣和下装不太受天气限制（只有热天会排除厚的）
- 点「换一套」会避开前 3 套里出现过的衣服
- 外套会在保暖度相近的几件里轮换；在场合里写了温度（如「20度」），外套也按这个温度选
- 丝袜只在可爱风穿裙子时偶尔出现
- **场合输入**：写下要去哪（中文或英文），按关键词调整推荐，例如「约会 室内20度」「去健身房」「面试」「圣诞市场 户外」「在家」「dinner, I feel the cold」
- **叠穿**：零下时羽绒服里加一件中层（开衫或 Scuba）；冷天卫衣里可以加一件 T 恤（不加长袖）；穿连衣裙时只配外套
- **待洗**：每件衣服可以标「待洗」暂时不推荐，洗好再放回
- **轮换**：点「今天就穿这套 ✓」记录已穿；没穿过的优先，一类衣服全穿过一轮后重新开始（外套除外）
- **不喜欢这套 👎**：记住这套里上衣/下装/鞋的两两组合，以后不再这样配
- 搭配规则：下装和鞋要和上衣有共同风格；上衣和下装最多一件有花纹
- 待洗、已穿、不喜欢的记录只存在当前浏览器

## clothes.json

照片放 `photos/`，在 `clothes.json` 里登记：

```json
{"name": "米色小狗卫衣", "name_en": "Beige dog sweatshirt", "cat": "top", "warmth": 3,
 "waterproof": false, "styles": ["cute", "casual"], "file": "dog-sweatshirt.jpg"}
```

- `cat`：outer 外套 / top 上衣 / dress 连衣裙 / bottom 下装 / legs 袜子打底 / shoes 鞋 / acc 配饰(帽/围巾/手套)
- `warmth`：1 很薄 … 5 很厚
- `styles`：cute 可爱 / sport 运动 / formal 正式 / casual 日常，用于 Go out 和场合输入
- `pattern`（可选）：true 表示格子/条纹/印花，上衣和下装最多一件有花纹
- `layer`（可选）：`mid` 可以穿在羽绒服里面
- `kind`：配饰写 hat / scarf / gloves；T 恤写 `tee`，所有 T 恤都可以穿在卫衣里面
- 网页里临时上传的照片只存在当前浏览器（IndexedDB），不会进仓库
- `weather.py`：命令行查看杜伦天气

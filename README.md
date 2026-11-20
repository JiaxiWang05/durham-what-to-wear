# durham-what-to-wear

根据杜伦 (Durham, UK) 当天天气，从自己的衣服库里推荐穿搭，并把衣服拼在一起预览。页面右上角可切换 English / 中文。

Outfit picks from your own wardrobe for today's weather in Durham, UK, with a flat-lay preview. Toggle English / 中文 at the top right.

- 打开 / Open: https://jiaxiwang05.github.io/durham-what-to-wear/
- 天气来自 [Open-Meteo](https://open-meteo.com/)（免费，无需 key），按白天 08–20 点体感温度和降水概率推荐
- **日常 / Go out ✨**：Go out 只选可爱款，里面按室内 15–22°C 搭配，外套仍按真实天气
- **场合输入**：写下要去哪（中文或英文），按关键词调整推荐，例如「约会 室内20度」「去健身房」「面试」「圣诞市场 户外」「在家」「dinner, I feel the cold」
- **叠穿**：零下时外套里加一件中层；冷天卫衣里加衬衫/长袖，薄连衣裙里加长袖
- **待洗**：每件衣服可以标「待洗」暂时不推荐，洗好再放回
- **轮换**：点「今天就穿这套 ✓」记录已穿；没穿过的优先，一类衣服全穿过一轮后重新开始（外套除外）
- 待洗和已穿记录只存在当前浏览器

## clothes.json

照片放 `photos/`，在 `clothes.json` 里登记：

```json
{"name": "米色小狗卫衣", "name_en": "Beige dog sweatshirt", "cat": "top", "warmth": 3,
 "waterproof": false, "styles": ["cute", "casual"], "file": "dog-sweatshirt.jpg"}
```

- `cat`：outer 外套 / top 上衣 / dress 连衣裙 / bottom 下装 / legs 袜子打底 / shoes 鞋 / acc 配饰(帽/围巾/手套)
- `warmth`：1 很薄 … 5 很厚
- `styles`：cute 可爱 / sport 运动 / formal 正式 / casual 日常，用于 Go out 和场合输入
- `layer`（可选）：`base` 可以穿在卫衣或连衣裙里面；`mid` 可以穿在羽绒服里面
- 网页里临时上传的照片只存在当前浏览器（IndexedDB），不会进仓库
- `weather.py`：命令行查看杜伦天气

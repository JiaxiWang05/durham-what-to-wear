# durham-what-to-wear

根据杜伦 (Durham, UK) 当天天气，从你自己的衣服库里推荐穿搭，并把衣服拼在一起预览。

- 打开：https://jiaxiwang05.github.io/durham-what-to-wear/
- 上传衣服照片，选类别（外套/上衣/下装/鞋/配饰）和保暖度 1–5，可勾“防水”
- 天气来自 [Open-Meteo](https://open-meteo.com/)（免费，无需 key），按白天 08–20 点体感温度和降水概率推荐
- 衣服库在仓库里：照片放 `photos/`，在 `clothes.json` 里登记，所有设备打开都能看到（公开）
  ```json
  [{"file": "coat1.jpg", "cat": "outer", "warmth": 4, "waterproof": true, "name": "绿色外套"}]
  ```
  `cat`：outer 外套 / top 上衣 / dress 连衣裙 / bottom 下装 / legs 袜子打底 / shoes 鞋 / acc 配饰(帽/围巾/手套)
  `cute`：true 表示适合 Go out 模式（可爱风，室内约 15°C 搭配）
- 网页里临时上传的照片只存在当前浏览器（IndexedDB），不会进仓库
- 预览：外套在后、上衣叠在前，下面是裤子和鞋，只是平铺示意，不是真人试穿
- `weather.py`：命令行查看杜伦天气

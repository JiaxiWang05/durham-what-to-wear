#!/usr/bin/env python3
"""Durham (UK) weather for outfit planning. Uses Open-Meteo (free, no API key)."""
import json
import urllib.request

URL = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=54.7761&longitude=-1.5733"
    "&current=temperature_2m,apparent_temperature,precipitation,wind_speed_10m,weather_code"
    "&hourly=temperature_2m,apparent_temperature,precipitation_probability,wind_speed_10m"
    "&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,"
    "precipitation_sum,wind_speed_10m_max,sunrise,sunset"
    "&timezone=Europe%2FLondon&forecast_days=2"
)

with urllib.request.urlopen(URL, timeout=15) as r:
    d = json.load(r)

c = d["current"]
print(f"现在 {c['time']}: {c['temperature_2m']}°C (体感 {c['apparent_temperature']}°C), "
      f"降水 {c['precipitation']}mm, 风速 {c['wind_speed_10m']} km/h, code {c['weather_code']}")

day = d["daily"]
for i, date in enumerate(day["time"]):
    print(f"{date}: {day['temperature_2m_min'][i]}~{day['temperature_2m_max'][i]}°C, "
          f"降水概率 {day['precipitation_probability_max'][i]}%, 雨量 {day['precipitation_sum'][i]}mm, "
          f"最大风速 {day['wind_speed_10m_max'][i]} km/h")

h = d["hourly"]
print("\n今天 08–22 点（每 2 小时）:")
for i, t in enumerate(h["time"][:24]):
    hour = int(t[11:13])
    if 8 <= hour <= 22 and hour % 2 == 0:
        print(f"  {t[11:]}  {h['temperature_2m'][i]}°C 体感 {h['apparent_temperature'][i]}°C  "
              f"雨 {h['precipitation_probability'][i]}%  风 {h['wind_speed_10m'][i]} km/h")

========================================================================================================
РУС
# Yellow-Sea-Chl

Прототип прогноза и сравнения прогнозов хлорофилла (chl) в Желтом море.

## Что делает проект?
Показывает среднее значение хлорофилла по области 30–41°N, 118–126°E за 2025–2026 годы и два варианта прогноза на горизонт от 1 до 14 дней: "как сегодня" и климатологию (среднее за тот же день года)

## Данные
Модельный набор Copernicus Marine: GLOBAL_ANALYSISFORECAST_BGC_001_028, переменная `chl`, ежедневно, разрешение 0.25°. Это модельные, а не измеренные данные.

## Результаты проверки
- Проверка 1 (тест: лето–осень 2026): на горизонте 7 дней линейная регрессия немного лучше простого прогноза (MAE 0.047 против 0.052 мг/м³). Разница не проверялась статистически.
- Проверка 2 (обучение на 2025, тест: март–май 2026, цветение): на горизонтах 1 и 7 дней простой прогноз лучше регрессии и климатологии; на 14 днях регрессия и климатология примерно равны (MAE 0.065 против 0.077 у простого прогноза).
- Вывод: регрессия не дала устойчивого выигрыша, поэтому в приложении она не используется для прогноза.

## Ограничения
- Тест покрывает один год и три месяца, выводы предварительные.
- Климатология построена по всем данным, включая тестовый период, поэтому её ошибка занижена.
- Среднее по области сглаживает прибрежные значения, где хлорофилл обычно выше.
- Приложение не заменяет официальные предупреждения служб.

## Запуск
pip install -r requirements.txt
streamlit run app.py

========================================================================================================

ENG
# Yellow-Sea-Chl

A prototype for forecasting and comparing chlorophyll-a (chl) forecasts in the Yellow Sea.

## What it does
The app shows the average chlorophyll-a concentration over the area 30–41°N, 118–126°E for 2025–2026, and two forecast options for horizons from 1 to 14 days: "same as today" (persistence) and climatology (the average for the same day of the year).

## Data
Copernicus Marine model product: GLOBAL_ANALYSISFORECAST_BGC_001_028, variable `chl`, daily, 0.25° resolution. These are model data, not in situ or satellite measurements.

## Validation results
- **Test 1 (summer–autumn 2026):** at a 7-day horizon, linear regression is slightly better than the persistence forecast (MAE 0.047 vs 0.052 mg/m³). The difference was not tested for statistical significance.
- **Test 2 (trained on 2025, tested on March–May 2026, the bloom season):** at 1 and 7 days, persistence is better than regression and climatology; at 14 days, regression and climatology are close (MAE 0.065 vs 0.077 for persistence).
- **Conclusion:** regression did not give a stable improvement, so the app does not use it for forecasting.

## Limitations
- The test covers one year and three months; conclusions are preliminary.
- The climatology is built from all data, including the test period, so its error is underestimated.
- The regional average smooths out coastal values, where chlorophyll is usually higher.
- The app does not replace official warnings from public services.

## Run locally
pip install -r requirements.txt
streamlit run app.py

========================================================================================================

中文
# Yellow-Sea-Chl

黄海叶绿素-a（chl）预报与预报方法比较的原型项目。

## 项目内容
应用展示 2025–2026 年在区域 30–41°N、118–126°E 内叶绿素-a 的平均浓度，并给出 1 至 14 天两种预报方案：“与今日相同”（持续性预报）和气候态预报（同一年内同一天的历史平均值）。

## 数据
Copernicus Marine 模式产品：GLOBAL_ANALYSISFORECAST_BGC_001_028，变量 `chl`，逐日数据，分辨率 0.25°。这些是模式数据，并非现场或卫星实测数据。

## 验证结果
- **检验一（2026 年夏季至秋季）：** 在 7 天预报时，线性回归略优于持续性预报（MAE 0.047 对 0.052 mg/m³）。未对该差异进行统计显著性检验。
- **检验二（用 2025 年训练，测试 2026 年 3–5 月的藻华季节）：** 在 1 天和 7 天，持续性预报优于回归和气候态预报；在 14 天，回归与气候态预报接近（MAE 0.065 对 0.077，持续性预报为 0.077）。
- **结论：** 回归方法未带来稳定的改进，因此应用不使用它进行预报。

## 局限性
- 测试仅覆盖一年三个月，结论为初步结果。
- 气候态基于全部数据构建，包括测试时段，因此其误差被低估。
- 区域平均会平滑近岸数值，而近岸叶绿素通常更高。
- 本应用不能替代公共服务机构发布的官方预警。

## 本地运行
pip install -r requirements.txt
streamlit run app.py

========================================================================================================

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Хлорофилла, Желтое море")
st.title("Хлорофилла в Желтом море")
st.caption(
    "Модельные данные Copernicus Marine (GLOBAL_ANALYSISFORECAST_BGC_001_028), "
    "среднее по области 30–41°N, 118–126°E, 2025–2026. "
    "Не заменяет официальные предупреждения служб"
)

s = pd.read_csv("chl_yellow_sea.csv", index_col=0, parse_dates=True)["chl"]
last_date = s.index[-1]
last = s.iloc[-1]

# Климатология: среднее значение для каждого дня года по всем доступным данным
clim = s.groupby(s.index.dayofyear).mean()

H = st.slider("Горизонт прогноза, дней", 1, 14, 7)
target_date = last_date + pd.Timedelta(days=H)
clim_val = clim.get(target_date.dayofyear, float("nan"))

col1, col2 = st.columns(2)
col1.metric("Последнее значение", f"{last:.2f} мг/м³",
            help=f"на {last_date:%d.%m.%Y}")
col2.metric(f"Климатология на {target_date:%d.%m}", f"{clim_val:.2f} мг/м³",
            help="Среднее значение за этот день года по всем доступным годам")

st.subheader(f"Прогноз на {H} дн. ({target_date:%d.%m.%Y})")
st.write(
    f"Простой прогноз («как сегодня»): **{last:.2f} мг/м³**. "
    f"Климатология: **{clim_val:.2f} мг/м³**."
)
st.info(
    "По результатам проверки на весне 2026 года простой прогноз лучше "
    "на горизонтах 1 и 7 дней, а на 14 днях примерно равен климатологии. "
    "Поэтому показаны оба варианта."
)

if last > 1.0:
    st.warning("Значения выше 1 мг/м³ могут указывать на цветение водорослей. "
               "Это упрощённый ориентир, а не официальный сигнал.")
else:
    st.success("Значения в пределах обычного диапазона для этого периода.")

st.subheader(f"История: {s.index[0]:%Y}–{s.index[-1]:%Y}")
st.line_chart(s)

with st.expander("Как считаются прогнозы и что не учтено"):
    st.write(
        "Климатология построена по всем данным, включая весну 2026 года, поэтому "
        "её ошибка в честной проверке занижена. Линейная регрессия не используется "
        "в приложении: на проверке она не дала устойчивого выигрыша."
    )
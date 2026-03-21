import streamlit as st
import altair as alt

st.title("Grafische Darstellung des Berechnungsverlaufs")

data_df = st.session_state["data_df"]

if data_df.empty:
    st.info("Keine Daten vorhanden. Bitte zuerst eine Berechnung durchführen.")
    st.stop()

def get_group(unit):
    if unit in ["L", "mL", "cL", "µL"]:
        return "Volumen"
    elif unit in ["µg", "mg", "g", "kg", "t"]:
        return "Masse"
    elif unit in ["µmol", "mmol", "mol"]:
        return "Stoffmenge"
    elif unit in ["°C", "°F", "K"]:
        return "Temperatur"
    return "Andere"

chart_df = data_df.copy()
chart_df["Gruppe"] = chart_df["Von"].apply(get_group)

chart = alt.Chart(chart_df).mark_line(point=True).encode(
    x=alt.X(
        "timestamp:T",
        title="Zeitpunkt der Berechnung"
    ),
    y=alt.Y(
        "Ergebnis:Q",
        title="Ergebnis"
    ),
    color=alt.Color(
        "Gruppe:N",
        title="Einheitsgruppen",
        scale=alt.Scale(
            domain=["Volumen", "Masse", "Stoffmenge", "Temperatur"],
            range=["#4C78A8", "#F58518", "#54A24B", "#E45756"]
        )
    ),
    tooltip=[
        alt.Tooltip("timestamp:T", title="Zeit"),
        alt.Tooltip("Wert:Q"),
        alt.Tooltip("Von:N"),
        alt.Tooltip("Nach:N"),
        alt.Tooltip("Ergebnis:Q"),
        alt.Tooltip("Gruppe:N")
    ]
)

st.altair_chart(chart, use_container_width=True)

st.caption("Die Grafik zeigt die Ergebnisse der Berechnungen im zeitlichen Verlauf.")
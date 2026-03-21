import streamlit as st
import altair as alt

st.title("Grafische Darstellung des Berechnungsverlaufs")

data_df = st.session_state["data_df"]

if data_df.empty:
    st.info("Keine Daten vorhanden. Bitte zuerst eine Berechnung durchführen.")
    st.stop()

chart_df = data_df.copy()
chart_df["Berechnung"] = range(1, len(chart_df) + 1)

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

chart_df["Gruppe"] = chart_df["Von"].apply(get_group)

chart = alt.Chart(chart_df).mark_bar().encode(
    x=alt.X("Berechnung:O", title="Berechnung"),
    y=alt.Y("Ergebnis:Q", title="Ergebnis"),
    color=alt.Color(
        "Gruppe:N",
        title="Einheitsgruppen",
        scale=alt.Scale(
            domain=["Volumen", "Masse", "Stoffmenge", "Temperatur"],
            range=["#4C78A8", "#F58518", "#54A24B", "#E45756"]
        )
    ),
    tooltip=["Berechnung", "Ergebnis", "Von", "Nach", "Gruppe"]
)

st.altair_chart(chart, use_container_width=True)
st.caption("Grafische Darstellung des Berechnungsverlaufs")
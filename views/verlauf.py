import streamlit as st
import altair as alt

st.title("Grafische Darstellung des Berechnungsverlaufs")

# Daten holen
if "data_df" not in st.session_state or st.session_state["data_df"].empty:
    st.info("Keine Daten vorhanden. Bitte zuerst eine Berechnung durchführen.")
    st.stop()

data_df = st.session_state["data_df"]


# -------- Einheitsgruppen bestimmen --------
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


# -------- Daten vorbereiten --------
chart_df = data_df.copy()

# Gruppe hinzufügen
chart_df["Gruppe"] = chart_df["Von"].apply(get_group)

# ⭐ WICHTIG: Berechnungsnummer statt Zeit
chart_df["Berechnungsnummer"] = range(1, len(chart_df) + 1)


# -------- Diagramm --------
chart = alt.Chart(chart_df).mark_line(point=True).encode(
    x=alt.X(
    "Berechnungsnummer:Q",
    title="Berechnungsnummer",
    axis=alt.Axis(
        tickMinStep=1,
        format="d"
    )
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
        alt.Tooltip("Berechnungsnummer:Q", title="Nr."),
        alt.Tooltip("Wert:Q"),
        alt.Tooltip("Von:N"),
        alt.Tooltip("Nach:N"),
        alt.Tooltip("Ergebnis:Q"),
        alt.Tooltip("Gruppe:N")
    ]
)

st.altair_chart(chart, use_container_width=True)

# -------- Beschreibung --------
st.caption("Die Grafik zeigt die Ergebnisse der Berechnungen in der Reihenfolge Ihrer Durchführung.")
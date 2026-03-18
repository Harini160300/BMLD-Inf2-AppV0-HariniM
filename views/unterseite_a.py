import streamlit as st
from functions import Einheitenrechner as sm
from pathlib import Path
import pandas as pd
from datetime import datetime
from utils.data_manager import DataManager
import pytz

user = st.session_state.get("username", "unknown")


# -------- Umrechnungsfunktion --------
def umrechnen(val: float, src: str, dst: str) -> float:

    val = float(val)

    if src == dst:
        return val

    # ---- Volumen ----
    if src == "L" and dst == "mL":
        return sm.l_to_ml(val)
    if src == "mL" and dst == "L":
        return sm.ml_to_l(val)

    if src == "L" and dst == "cL":
        return sm.l_to_cl(val)
    if src == "cL" and dst == "L":
        return sm.cl_to_l(val)

    if src == "L" and dst == "µL":
        return sm.l_to_ul(val)
    if src == "µL" and dst == "L":
        return sm.ul_to_l(val)

    if src == "mL" and dst == "cL":
        return sm.ml_to_cl(val)
    if src == "cL" and dst == "mL":
        return sm.cl_to_ml(val)

    if src == "mL" and dst == "µL":
        return sm.ml_to_ul(val)
    if src == "µL" and dst == "mL":
        return sm.ul_to_ml(val)

    if src == "cL" and dst == "µL":
        return sm.cl_to_ul(val)
    if src == "µL" and dst == "cL":
        return sm.ul_to_cl(val)

    # ---- Masse ----
    if src == "µg" and dst == "mg":
        return sm.ug_to_mg(val)
    if src == "mg" and dst == "µg":
        return sm.mg_to_ug(val)

    if src == "µg" and dst == "g":
        return sm.ug_to_g(val)
    if src == "g" and dst == "µg":
        return sm.g_to_ug(val)

    if src == "µg" and dst == "kg":
        return sm.ug_to_kg(val)
    if src == "kg" and dst == "µg":
        return sm.kg_to_ug(val)

    if src == "µg" and dst == "t":
        return sm.ug_to_t(val)
    if src == "t" and dst == "µg":
        return sm.t_to_ug(val)

    if src == "mg" and dst == "g":
        return sm.mg_to_g(val)
    if src == "g" and dst == "mg":
        return sm.g_to_mg(val)

    if src == "mg" and dst == "kg":
        return sm.mg_to_kg(val)
    if src == "kg" and dst == "mg":
        return sm.kg_to_mg(val)

    if src == "mg" and dst == "t":
        return sm.mg_to_t(val)
    if src == "t" and dst == "mg":
        return sm.t_to_mg(val)

    if src == "g" and dst == "kg":
        return sm.g_to_kg(val)
    if src == "kg" and dst == "g":
        return sm.kg_to_g(val)

    if src == "g" and dst == "t":
        return sm.g_to_t(val)
    if src == "t" and dst == "g":
        return sm.t_to_g(val)

    if src == "kg" and dst == "t":
        return sm.kg_to_t(val)
    if src == "t" and dst == "kg":
        return sm.t_to_kg(val)

    # ---- Stoffmenge ----
    if src == "mol" and dst == "mmol":
        return sm.mol_to_mmol(val)
    if src == "mmol" and dst == "mol":
        return sm.mmol_to_mol(val)

    if src == "mol" and dst == "µmol":
        return sm.mol_to_umol(val)
    if src == "µmol" and dst == "mol":
        return sm.umol_to_mol(val)

    if src == "mmol" and dst == "µmol":
        return sm.mmol_to_umol(val)
    if src == "µmol" and dst == "mmol":
        return sm.umol_to_mmol(val)

    # ---- Temperatur ----
    if src == "°C" and dst == "°F":
        return sm.celsius_to_fahrenheit(val)
    if src == "°F" and dst == "°C":
        return sm.fahrenheit_to_celsius(val)

    if src == "°C" and dst == "K":
        return sm.celsius_to_kelvin(val)
    if src == "K" and dst == "°C":
        return sm.kelvin_to_celsius(val)

    if src == "°F" and dst == "K":
        return sm.fahrenheit_to_kelvin(val)
    if src == "K" and dst == "°F":
        return sm.kelvin_to_fahrenheit(val)

    raise ValueError("Diese Umrechnung wird nicht unterstützt")


def format_result(value: float, unit: str) -> str:
    if unit in ["°C", "°F", "K"]:
        return f"{value:.2f}"
    return f"{value:.6g}"


# -------- Reset-Funktion --------
def reset_form():
    st.session_state["value_input"] = 0.0
    st.session_state["from_unit_input"] = "L"
    st.session_state["to_unit_input"] = "mL"
    st.session_state["last_result"] = None
    st.session_state["feedback"] = None


# -------- Session State --------
if "value_input" not in st.session_state:
    st.session_state["value_input"] = 0.0

if "from_unit_input" not in st.session_state:
    st.session_state["from_unit_input"] = "L"

if "to_unit_input" not in st.session_state:
    st.session_state["to_unit_input"] = "mL"

if "last_result" not in st.session_state:
    st.session_state["last_result"] = None

if "feedback" not in st.session_state:
    st.session_state["feedback"] = None

if "calc_id" not in st.session_state:
    st.session_state["calc_id"] = 0

if "balloons_shown_for" not in st.session_state:
    st.session_state["balloons_shown_for"] = -1

if "data_df" not in st.session_state:
    st.session_state["data_df"] = pd.DataFrame(
        columns=["timestamp", "Wert", "Von", "Nach", "Ergebnis"]
    )


# -------- UI --------
st.title("Einheitenrechner")

units = [
    "L", "mL", "cL", "µL",
    "µg", "mg", "g", "kg", "t",
    "µmol", "mmol", "mol",
    "°C", "°F", "K"
]

with st.form("convert_form"):
    value = st.number_input(
        "Wert",
        key="value_input",
        format="%.6g"
    )

    from_unit = st.selectbox(
        "Von (Einheit)",
        units,
        key="from_unit_input"
    )

    to_unit = st.selectbox(
        "Nach (Einheit)",
        units,
        key="to_unit_input"
    )

    show_balloons = st.checkbox(
        "Ballons anzeigen beim Ergebnis",
        value=True
    )

    col1, col2 = st.columns(2)

    with col1:
        submit = st.form_submit_button("Berechnen")

    with col2:
        reset = st.form_submit_button("Reset", on_click=reset_form)

# -------- Berechnen --------
if submit:
    try:
        result = umrechnen(value, from_unit, to_unit)

        # Ergebnis speichern
        st.session_state["last_result"] = (value, from_unit, to_unit, result)
        st.session_state["feedback"] = None
        st.session_state["calc_id"] += 1

        result_row = {
            "timestamp": datetime.now(pytz.timezone("Europe/Zurich")),
            "Wert": value,
            "Von": from_unit,
            "Nach": to_unit,
            "Ergebnis": result
        }

        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result_row])],
            ignore_index=True
        )

       # Persistentes Speichern
        data_manager = DataManager()
        filename = f"{user.replace(' ', '_')}.csv"
        data_manager.save_user_data(st.session_state["data_df"], filename)

    except Exception as e:
        st.session_state["last_result"] = ("__error__", str(e))


# -------- Ergebnis anzeigen --------
if st.session_state["last_result"] is not None:

    lo = st.session_state["last_result"]

    if lo[0] == "__error__":
        st.error(lo[1])

    else:
        v, src, dst, res = lo
        out = format_result(res, dst)

        st.success(f"{v} {src} = {out} {dst}")

        if (
            show_balloons
            and st.session_state["balloons_shown_for"] != st.session_state["calc_id"]
        ):
            st.balloons()
            st.session_state["balloons_shown_for"] = st.session_state["calc_id"]

        st.info("Berechnung abgeschlossen! Vielen Dank für die Nutzung unseres Einheitenrechners.")
        
        st.divider()


# -------- Feedback --------
st.subheader("War die App hilfreich?")

col1, col2 = st.columns(2)

with col1:
    if st.button("👍 Ja hilfreich"):
        st.session_state["feedback"] = "up"

with col2:
    if st.button("👎 Nein"):
        st.session_state["feedback"] = "down"


# -------- Feedback Reaktion --------
if st.session_state.get("feedback") == "up":

    st.success("Aww danke! Wir freuen uns, dass die App dir geholfen hat.")

    st.markdown(
        """
        <div style="text-align:center;">
            <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExODg2MDg5bnNwbDhzbGE3eDRienkxN3ZwYzIybm4xdTd1c2U2NjdyeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TCKxvBY0MA3uKzXdeo/giphy.gif" width="260">
        </div>
        """,
        unsafe_allow_html=True
    )

elif st.session_state.get("feedback") == "down":

    st.warning("Danke für dein Feedback! Wir verbessern die App weiter.")

    img_path = Path(__file__).parent / "elefant_feedback.png"

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(str(img_path), width=250)


# -------- Berechnungsverlauf --------
st.subheader("Berechnungsverlauf")

st.caption("Alle bisherigen Berechnungen werden hier angezeigt.")

st.dataframe(st.session_state["data_df"])


# -------- Grafik --------
st.subheader("Verlauf der Ergebnisse")

if not st.session_state["data_df"].empty:
    st.line_chart(st.session_state["data_df"]["Ergebnis"])
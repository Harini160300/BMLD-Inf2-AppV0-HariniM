import pandas as pd
import streamlit as st
from pathlib import Path

from utils.data_manager import DataManager
from functions.Einheitenrechner import calculate_conversion


def format_result(value: float, unit: str) -> str:
    if unit in ["°C", "°F", "K"]:
        return f"{value:.2f}"
    return f"{value:.6g}"


def reset_form():
    st.session_state["value_input"] = 0.0
    st.session_state["from_unit_input"] = "L"
    st.session_state["to_unit_input"] = "mL"
    st.session_state["last_result"] = None
    st.session_state["feedback"] = None
    st.session_state["calc_id"] = 0
    st.session_state["balloons_shown_for"] = -1
    st.session_state["data_df"] = pd.DataFrame()


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
        columns=["Wert", "Von", "Nach", "Ergebnis"]
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
    value = st.number_input("Wert", key="value_input", format="%.6g")

    from_unit = st.selectbox("Von (Einheit)", units, key="from_unit_input")
    to_unit = st.selectbox("Nach (Einheit)", units, key="to_unit_input")

    show_balloons = st.checkbox("Ballons anzeigen beim Ergebnis", value=True)

    col1, col2 = st.columns(2)
    with col1:
        submitted = st.form_submit_button("Berechnen")
    with col2:
        reset = st.form_submit_button("Reset", on_click=reset_form)


# -------- Berechnung --------
if submitted:
    try:
        result = calculate_conversion(value, from_unit, to_unit)

        st.session_state["last_result"] = (
            result["Wert"],
            result["Von"],
            result["Nach"],
            result["Ergebnis"]
        )

        st.session_state["feedback"] = None
        st.session_state["calc_id"] += 1

        st.session_state["data_df"] = pd.concat(
            [st.session_state["data_df"], pd.DataFrame([result])],
            ignore_index=True
        )

        data_manager = DataManager()
        data_manager.save_user_data(st.session_state["data_df"], "data.csv")

    except Exception as e:
        st.session_state["last_result"] = ("__error__", str(e))


# -------- Ergebnis --------
if st.session_state["last_result"] is not None:
    lo = st.session_state["last_result"]

    if lo[0] == "__error__":
        st.error(lo[1])
    else:
        v, src, dst, res = lo
        out = format_result(res, dst)

        st.success(f"{v} {src} = {out} {dst}")

        if show_balloons and st.session_state["balloons_shown_for"] != st.session_state["calc_id"]:
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


# -------- Verlauf Tabelle --------
st.subheader("Berechnungsverlauf")
st.caption("Alle bisherigen Berechnungen werden hier angezeigt.")
st.dataframe(st.session_state["data_df"])


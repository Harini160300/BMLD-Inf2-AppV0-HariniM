import streamlit as st
from functions import Einheitenrechner as sm


# -------- Umrechnungsfunktion --------
def umrechnen(val: float, src: str, dst: str) -> float:

    val = float(val)

    if src == dst:
        return val


    # ---- Volumen ----
    if src == "L" and dst == "mL": return sm.l_to_ml(val)
    if src == "mL" and dst == "L": return sm.ml_to_l(val)

    if src == "L" and dst == "cL": return sm.l_to_cl(val)
    if src == "cL" and dst == "L": return sm.cl_to_l(val)

    if src == "L" and dst == "µL": return sm.l_to_ul(val)
    if src == "µL" and dst == "L": return sm.ul_to_l(val)

    if src == "mL" and dst == "cL": return sm.ml_to_cl(val)
    if src == "cL" and dst == "mL": return sm.cl_to_ml(val)

    if src == "mL" and dst == "µL": return sm.ml_to_ul(val)
    if src == "µL" and dst == "mL": return sm.ul_to_ml(val)

    if src == "cL" and dst == "µL": return sm.cl_to_ul(val)
    if src == "µL" and dst == "cL": return sm.ul_to_cl(val)


    # ---- Masse ----
    if src == "µg" and dst == "mg": return sm.ug_to_mg(val)
    if src == "mg" and dst == "µg": return sm.mg_to_ug(val)

    if src == "µg" and dst == "g": return sm.ug_to_g(val)
    if src == "g" and dst == "µg": return sm.g_to_ug(val)

    if src == "µg" and dst == "kg": return sm.ug_to_kg(val)
    if src == "kg" and dst == "µg": return sm.kg_to_ug(val)

    if src == "µg" and dst == "t": return sm.ug_to_t(val)
    if src == "t" and dst == "µg": return sm.t_to_ug(val)

    if src == "mg" and dst == "g": return sm.mg_to_g(val)
    if src == "g" and dst == "mg": return sm.g_to_mg(val)

    if src == "mg" and dst == "kg": return sm.mg_to_kg(val)
    if src == "kg" and dst == "mg": return sm.kg_to_mg(val)

    if src == "mg" and dst == "t": return sm.mg_to_t(val)
    if src == "t" and dst == "mg": return sm.t_to_mg(val)

    if src == "g" and dst == "kg": return sm.g_to_kg(val)
    if src == "kg" and dst == "g": return sm.kg_to_g(val)

    if src == "g" and dst == "t": return sm.g_to_t(val)
    if src == "t" and dst == "g": return sm.t_to_g(val)

    if src == "kg" and dst == "t": return sm.kg_to_t(val)
    if src == "t" and dst == "kg": return sm.t_to_kg(val)


    # ---- Stoffmenge ----
    if src == "mol" and dst == "mmol": return sm.mol_to_mmol(val)
    if src == "mmol" and dst == "mol": return sm.mmol_to_mol(val)

    if src == "mol" and dst == "µmol": return sm.mol_to_umol(val)
    if src == "µmol" and dst == "mol": return sm.umol_to_mol(val)

    if src == "mmol" and dst == "µmol": return sm.mmol_to_umol(val)
    if src == "µmol" and dst == "mmol": return sm.umol_to_mmol(val)


    # ---- Temperatur ----
    if src == "°C" and dst == "°F": return sm.celsius_to_fahrenheit(val)
    if src == "°F" and dst == "°C": return sm.fahrenheit_to_celsius(val)

    if src == "°C" and dst == "K": return sm.celsius_to_kelvin(val)
    if src == "K" and dst == "°C": return sm.kelvin_to_celsius(val)

    if src == "°F" and dst == "K": return sm.fahrenheit_to_kelvin(val)
    if src == "K" and dst == "°F": return sm.kelvin_to_fahrenheit(val)


    raise ValueError("Diese Umrechnung wird nicht unterstützt")


def format_result(value: float, unit: str):

    if unit in ["°C","°F","K"]:
        return f"{value:.2f}"

    return f"{value:.6g}"


# -------- UI --------

st.title("Einheitenrechner")

units = [
"L","mL","cL","µL",
"µg","mg","g","kg","t",
"µmol","mmol","mol",
"°C","°F","K"
]

with st.form("convert_form"):

    value = st.number_input("Wert", value=0.0, format="%.6g")

    from_unit = st.selectbox("Von (Einheit)", units, index=0)

    to_unit = st.selectbox("Nach (Einheit)", units, index=1)

    show_balloons = st.checkbox("Ballons anzeigen", value=True)

    submit = st.form_submit_button("Berechnen")


if submit:

    try:

        result = umrechnen(value, from_unit, to_unit)

        out = format_result(result, to_unit)

        st.success(f"{value} {from_unit} = {out} {to_unit}")

        if show_balloons:
            st.balloons()

        st.info("🌟 Berechnung abgeschlossen!  \nVielen Dank für die Nutzung unseres Einheitenrechners und einen schönen Tag! 😊")

    except Exception as e:

        st.error(str(e))
import streamlit as st
from functions import Stoffmengenrechner as sm

# unterstützte Einheiten
units = [
    "L", "mL", "µL", "cL",
    "µg", "mg", "g", "kg", "t",
    "µmol", "mmol", "mol",
    "°C", "°F", "K",
]

st.title("Stoffmengenrechner")

st.write("Kurzbeschreibung: Einfache Einheiten- und Stoffmengen-Umrechnung. Wähle Einheit, Wert und drücke 'Berechnen'.")

with st.form(key="convert_form"):
    st.write("Eingaben")
    value = st.number_input("Wert", value=0.0, format="%.6g")
    from_unit = st.selectbox("Von (Einheit)", units, index=1)
    to_unit = st.selectbox("Nach (Einheit)", units, index=0)
    show_confetti = st.checkbox("Konfetti bei Ergebnis anzeigen", value=True)
    show_scientific = st.checkbox("Wissenschaftliche Notation verwenden", value=False)
    submit = st.form_submit_button("Berechnen")

if st.button("Erklärung anzeigen"):
    st.info(
        "Dieses Tool wandelt zwischen Volumen-, Masse-, Stoffmengen- und Temperatur-Einheiten um. "
        "Unterstützte Einheiten: L, mL, µL, cL, µg, mg, g, kg, t, µmol, mmol, mol, °C, °F, K."
    )

def umrechnen(val: float, src: str, dst: str) -> float:
    """Einfache Routing-Funktion, nutzt sm.* Funktionen."""
    if src == dst:
        return float(val)
    
        # Volumen
    if src == "L" and dst == "mL":
        return sm.l_to_ml(val)
    if src == "mL" and dst == "L":
        return sm.ml_to_l(val)
    if src == "mL" and dst == "µL":
        return sm.ml_to_ul(val)
    if src == "µL" and dst == "mL":
        return sm.ul_to_ml(val)
    if src == "cL" and dst == "mL":
        return float(val) * 10.0
    if src == "mL" and dst == "cL":
        return float(val) / 10.0
    if src == "cL" and dst == "L":
        return float(val) / 100.0
    if src == "L" and dst == "cL":
        return float(val) * 100.0
    
     # Masse
    if src == "mg" and dst == "g":
        return sm.mg_to_g(val)
    if src == "g" and dst == "mg":
        return sm.g_to_mg(val)
    if src == "g" and dst == "kg":
        return sm.g_to_kg(val)
    if src == "kg" and dst == "g":
        return sm.kg_to_g(val)
    if src == "kg" and dst == "t":
        return sm.kg_to_tonne(val)
    if src == "t" and dst == "kg":
        return sm.tonne_to_kg(val)
    if src == "µg" and dst == "mg":
        return sm.ug_to_mg(val)
    if src == "mg" and dst == "µg":
        return sm.mg_to_ug(val)

    # Stoffmengen
    if src == "mol" and dst == "mmol":
        return sm.mol_to_mmol(val)
    if src == "mmol" and dst == "mol":
        return sm.mmol_to_mol(val)
    if src == "mol" and dst == "µmol":
        return sm.mol_to_micromol(val)
    if src == "µmol" and dst == "mol":
        return sm.micromol_to_mol(val)

    # Temperatur
    if src == "°C" and dst == "°F":
        return sm.celsius_to_fahrenheit(val)
    if src == "°F" and dst == "°C":
        return sm.fahrenheit_to_celsius(val)
    if src == "°C" and dst == "K":
        return sm.celsius_to_kelvin(val)
    if src == "K" and dst == "°C":
        return sm.kelvin_to_celsius(val)

    raise ValueError(f"Umwandlung {src} → {dst} nicht unterstützt")

if submit:
    try:
        result = umrechnen(value, from_unit, to_unit)
        out = sm.format_number(result) if show_scientific else f"{result:.6g}"
        st.success(f"{value} {from_unit} = {out} {to_unit}")
        if show_confetti:
            st.balloons()
    except Exception as e:
        st.error(f"Fehler: {e}")
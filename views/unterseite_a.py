# ...existing code...
import streamlit as st
from functions import Einheitenrechner as sm

# --- Funktionen ZUERST ---

def umrechnen(val: float, src: str, dst: str) -> float:
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

    # Stoffmenge
    if src == "mol" and dst == "mmol":
        return sm.mol_to_mmol(val)
    if src == "mmol" and dst == "mol":
        return sm.mmol_to_mol(val)
    if src == "mol" and dst == "µmol":
        return sm.mol_to_micromol(val)
    if src == "µmol" and dst == "mol":
        return sm.micromol_to_mol(val)

  # ...existing code...
    # Temperatur
    if src == "°C" and dst == "°F":
        return sm.celsius_to_fahrenheit(val)
    if src == "°F" and dst == "°C":
        return sm.fahrenheit_to_celsius(val)
    if src == "°C" and dst == "K":
        return sm.celsius_to_kelvin(val)
    if src == "K" and dst == "°C":
        return sm.kelvin_to_celsius(val)
    # Neu: direkte Konversionen K <-> °F
    if src == "K" and dst == "°F":
        return sm.kelvin_to_fahrenheit(val)
    if src == "°F" and dst == "K":
        return sm.fahrenheit_to_kelvin(val)
# ...existing code...

    raise ValueError(f"Umwandlung {src} → {dst} nicht unterstützt")


# --- App Code DANACH ---

units = ["L","mL","µL","cL","µg","mg","g","kg","t","µmol","mmol","mol","°C","°F","K"]

st.title("Einheitenrechner")
st.write("Der Rechner ermöglicht die Umrechnung von Einheiten für Volumen, Masse, Temperatur und Stoffmenge (nur innerhalb derselben Gruppe).")

with st.form(key="convert_form"):
    st.write("Eingaben")
    value = st.number_input("Wert", value=0.0, format="%.6g")
    from_unit = st.selectbox("Von (Einheit)", units, index=1)
    to_unit = st.selectbox("Nach (Einheit)", units, index=0)
    show_balloon = st.checkbox("Ballon bei Ergebnis anzeigen")
    submit = st.form_submit_button("Berechnen")

# initiale Session-State Keys sicherstellen
if "last_output" not in st.session_state:
    st.session_state["last_output"] = None
if "last_error" not in st.session_state:
    st.session_state["last_error"] = None
if "output_shown" not in st.session_state:
    st.session_state["output_shown"] = False

# Wenn neu berechnet wurde: berechnen und Ergebnis in session_state speichern,
# und output_shown zurücksetzen (damit es einmal angezeigt wird).
if submit:
    st.session_state["output_shown"] = False
    try:
        result = umrechnen(value, from_unit, to_unit)
        st.session_state["last_output"] = (float(value), from_unit, to_unit, float(result))
        st.session_state["last_error"] = None
    except Exception as e:
        st.session_state["last_output"] = None
        st.session_state["last_error"] = str(e)

# Anzeige — nur einmal pro gespeicherter Berechnung
if st.session_state.get("last_output") and not st.session_state.get("output_shown"):
    v, src, dst, res = st.session_state["last_output"]
    out = f"{res:.2f}" if dst in ["°C","°F","K"] else f"{res:.6g}"
    st.success(f"{v} {src} = {out} {dst}")

    if show_balloon:
        st.balloons()

    # einfacher Dankestext (erscheint NUR hier, nach "Berechnen")
    st.info("Herzlichen Dank und einen schönen Tag")

    st.session_state["output_shown"] = True

if st.session_state.get("last_error") and not st.session_state.get("output_shown"):
    st.error(f"Fehler: {st.session_state['last_error']}")
    st.session_state["output_shown"] = True
# ...existing code...


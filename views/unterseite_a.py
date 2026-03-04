# ...existing code...
import streamlit as st
from functions import Einheitenrechner as sm

# ---- Umrechnungsfunktion ----
def umrechnen(val: float, src: str, dst: str) -> float:
    val = float(val)
    if src == dst:
        return val

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
        return val * 10.0
    if src == "mL" and dst == "cL":
        return val / 10.0
    if src == "cL" and dst == "L":
        return val / 100.0
    if src == "L" and dst == "cL":
        return val * 100.0

    # Masse
    if src == "µg" and dst == "mg":
        return sm.ug_to_mg(val)
    if src == "mg" and dst == "µg":
        return sm.mg_to_ug(val)
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

    # Stoffmenge
    if src == "mol" and dst == "mmol":
        return sm.mol_to_mmol(val)
    if src == "mmol" and dst == "mol":
        return sm.mmol_to_mol(val)
    if src == "mol" and dst == "µmol":
        return sm.mol_to_micromol(val)
    if src == "µmol" and dst == "mol":
        return sm.micromol_to_mol(val)
    if src == "mmol" and dst == "µmol":
        return val * 1000.0
    if src == "µmol" and dst == "mmol":
        return val / 1000.0

    # Temperatur (inkl. direkte K <-> °F falls vorhanden)
    if src == "°C" and dst == "°F":
        return sm.celsius_to_fahrenheit(val)
    if src == "°F" and dst == "°C":
        return sm.fahrenheit_to_celsius(val)
    if src == "°C" and dst == "K":
        return sm.celsius_to_kelvin(val)
    if src == "K" and dst == "°C":
        return sm.kelvin_to_celsius(val)
    if src == "K" and dst == "°F":
        return sm.kelvin_to_fahrenheit(val) if hasattr(sm, "kelvin_to_fahrenheit") else (val - 273.15) * 9.0 / 5.0 + 32.0
    if src == "°F" and dst == "K":
        return sm.fahrenheit_to_kelvin(val) if hasattr(sm, "fahrenheit_to_kelvin") else (val - 32.0) * 5.0 / 9.0 + 273.15

    raise ValueError(f"Umwandlung {src} → {dst} nicht unterstützt")

def _format_result(value: float, dst_unit: str) -> str:
    v = float(value)
    if dst_unit in {"°C","°F","K"}:
        return f"{v:.2f}"
    return f"{v:.6g}"

def _scientific_background(value: float, sig_digits: int = 6) -> str:
    try:
        v = float(value)
    except Exception:
        return str(value)
    if hasattr(sm, "format_float"):
        return sm.format_float(v, sig_digits=sig_digits)
    if hasattr(sm, "format_number"):
        return sm.format_number(v)
    return f"{v:.{sig_digits}g}"

# ---- UI ----
units = ["L","mL","µL","cL","µg","mg","g","kg","t","µmol","mmol","mol","°C","°F","K"]

st.set_page_config(page_title="Einheitenrechner")
st.title("Einheitenrechner")
st.subheader("Umrechnung von Volumen, Masse, Stoffmenge und Temperatur")

# session keys
if "last_output" not in st.session_state:
    st.session_state["last_output"] = None
if "output_shown" not in st.session_state:
    st.session_state["output_shown"] = False

with st.form(key="convert_form"):
    # Anzeige initial 0 (keine spätere programmgesteuerte Änderung des Widgets)
    value = float(st.number_input("Wert", value=0.0, format="%.6g"))
    from_unit = st.selectbox("Von (Einheit)", units, index=1)
    to_unit = st.selectbox("Nach (Einheit)", units, index=0)
    show_balloons = st.checkbox("Ballons bei Ergebnis anzeigen", value=True)
    submit = st.form_submit_button("Berechnen")

# Berechnung speichern; Anzeige erfolgt nur einmal
if submit:
    try:
        result = umrechnen(value, from_unit, to_unit)
        st.session_state["last_output"] = (float(value), from_unit, to_unit, float(result))
        st.session_state["output_shown"] = False
    except Exception as e:
        st.session_state["last_output"] = ("__error__", str(e))
        st.session_state["output_shown"] = False

# Anzeige: nur einmal pro Berechnung
if st.session_state.get("last_output") and not st.session_state.get("output_shown"):
    lo = st.session_state["last_output"]
    if lo[0] == "__error__":
        st.error(lo[1])
    else:
        v, src, dst, res = lo
        out = _format_result(res, dst)
        st.success(f"{v} {src} = {out} {dst}")
        if show_balloons:
            st.balloons()

        # Bild / SVG erscheint nach Berechnen
        st.markdown(
            """
            <div style="display:flex;justify-content:center;margin-top:12px">
            <svg width="300" height="180" viewBox="0 0 360 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Elefant">
              <ellipse cx="180" cy="200" rx="92" ry="18" fill="#cbdce4" opacity="0.35" />
              <g>
                <ellipse cx="140" cy="120" rx="92" ry="56" fill="#dfeff6" stroke="#7a8890" stroke-width="2"/>
                <rect x="90" y="155" rx="8" ry="8" width="26" height="36" fill="#b4c6ce"/>
                <rect x="160" y="155" rx="8" ry="8" width="26" height="36" fill="#b4c6ce"/>
              </g>
              <g transform="translate(220,86)">
                <circle cx="0" cy="0" r="46" fill="#dfeff6" stroke="#7a8890" stroke-width="2"/>
                <path d="M-28,-10 C-72,-18 -70,48 -18,50" fill="#f7dfe0" stroke="#7a8890" stroke-width="1.2"/>
                <circle cx="12" cy="-6" r="4.2" fill="#17202a"/>
                <circle cx="7" cy="-3" r="2" fill="#fff" opacity="0.9"/>
              </g>
              <g id="trunkRoot" transform="translate(240,100)">
                <path d="M0,0 C8,18 18,34 22,52 C24,64 16,70 6,72" fill="#e6f0f6" stroke="#7a8890" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                <circle cx="22" cy="52" r="6" fill="#b9d1db" stroke="#7a8890" stroke-width="1.0"/>
                <animateTransform xlink:href="#trunkRoot" attributeName="transform" type="rotate"
                  values="0 240 100; -22 240 100; 10 240 100; 0 240 100" dur="1.2s" repeatCount="indefinite" />
              </g>
            </svg>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Dankestext sichtbar nach Berechnung
        st.info("Thank you for using and have a nice day!")

    st.session_state["output_shown"] = True
# ...existing code...
  

  
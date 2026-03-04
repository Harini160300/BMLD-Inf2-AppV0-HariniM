import streamlit as st
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
    st.info("Dieses Tool wandelt zwischen Volumen-, Masse-, Stoffmengen- und Temperatur-Einheiten um. Unterstützte Einheiten: L, mL, µL, cL, µg, mg, g, kg, t, µmol, mmol, mol, °C, °F, K.")
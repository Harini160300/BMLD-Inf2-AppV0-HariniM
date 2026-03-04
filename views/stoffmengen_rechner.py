import streamlit as st

AVOGADRO = 6.02214076e23


def mass_to_mol(mass_g: float, molar_mass_g_per_mol: float) -> float:
    return mass_g / molar_mass_g_per_mol


def mol_to_mass(mol: float, molar_mass_g_per_mol: float) -> float:
    return mol * molar_mass_g_per_mol


def mol_to_particles(mol: float) -> float:
    return mol * AVOGADRO


def particles_to_mol(particles: float) -> float:
    return particles / AVOGADRO


def molarity_from_mol_and_volume(mol: float, volume_l: float) -> float:
    return mol / volume_l


def mol_from_molarity_and_volume(molarity: float, volume_l: float) -> float:
    return molarity * volume_l


def format_num(x: float) -> str:
    # Nicely format large/small numbers
    if x == 0:
        return "0"
    if abs(x) < 1e-3 or abs(x) >= 1e6:
        return f"{x:.4e}"
    return f"{x:.6f}".rstrip('0').rstrip('.')


def main():
    st.title("Stoffmengen-Rechner")
    st.write("Ein kleines Hilfsprogramm für Umrechnungen zwischen Masse, Stoffmenge (mol), Teilchenzahl und Molarität.")

    mode = st.selectbox("Rechenart:", [
        "Masse → Stoffmenge (mol)",
        "Stoffmenge (mol) → Masse",
        "Stoffmenge (mol) → Teilchenzahl",
        "Teilchenzahl → Stoffmenge (mol)",
        "Molarität (c) aus Stoffmenge und Volumen",
        "Stoffmenge aus Molarität und Volumen",
    ])

    if mode == "Masse → Stoffmenge (mol)":
        mass = st.number_input("Masse (g)", value=1.0, format="%f")
        mm = st.number_input("Molmasse / molare Masse (g/mol)", value=18.01528, format="%f")
        if mm <= 0:
            st.error("Die molare Masse muss größer als 0 sein.")
        else:
            mol = mass_to_mol(mass, mm)
            st.success(f"Stoffmenge: {format_num(mol)} mol")
            st.info(f"Das entspricht {format_num(mol_to_particles(mol))} Teilchen (Avogadro)")

    elif mode == "Stoffmenge (mol) → Masse":
        mol = st.number_input("Stoffmenge (mol)", value=1.0, format="%f")
        mm = st.number_input("Molmasse / molare Masse (g/mol)", value=18.01528, format="%f", key="mm2")
        if mm <= 0:
            st.error("Die molare Masse muss größer als 0 sein.")
        else:
            mass = mol_to_mass(mol, mm)
            st.success(f"Masse: {format_num(mass)} g")

    elif mode == "Stoffmenge (mol) → Teilchenzahl":
        mol = st.number_input("Stoffmenge (mol)", value=1.0, format="%f", key="mol3")
        particles = mol_to_particles(mol)
        st.success(f"Teilchenzahl: {format_num(particles)}")

    elif mode == "Teilchenzahl → Stoffmenge (mol)":
        particles = st.number_input("Teilchenzahl", value=6.02214076e23, format="%f")
        mol = particles_to_mol(particles)
        st.success(f"Stoffmenge: {format_num(mol)} mol")

    elif mode == "Molarität (c) aus Stoffmenge und Volumen":
        mol = st.number_input("Stoffmenge (mol)", value=1.0, format="%f", key="mol4")
        vol_ml = st.number_input("Volumen (mL)", value=1000.0, format="%f")
        if vol_ml <= 0:
            st.error("Volumen muss größer als 0 sein.")
        else:
            vol_l = vol_ml / 1000.0
            c = molarity_from_mol_and_volume(mol, vol_l)
            st.success(f"Molarität: {format_num(c)} mol/L")

    elif mode == "Stoffmenge aus Molarität und Volumen":
        c = st.number_input("Molarität (mol/L)", value=1.0, format="%f")
        vol_ml = st.number_input("Volumen (mL)", value=1000.0, format="%f", key="vol2")
        if vol_ml <= 0:
            st.error("Volumen muss größer als 0 sein.")
        else:
            vol_l = vol_ml / 1000.0
            mol = mol_from_molarity_and_volume(c, vol_l)
            st.success(f"Stoffmenge: {format_num(mol)} mol")

    st.markdown("---")
    st.write("Hinweis: Dieses Tool ist ein Lernwerkzeug. Bei wichtigen Laborrechnungen immer auf Einheiten und Genauigkeit achten.")


if __name__ == "__main__":
    main()

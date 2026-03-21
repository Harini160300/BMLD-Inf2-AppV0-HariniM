from datetime import datetime
import pytz


def _ensure_float(value: float, name: str) -> float:
    if value is None:
        raise ValueError(f"{name} darf nicht None sein")
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} muss eine Zahl sein")


def _ensure_non_negative(value: float, name: str) -> float:
    v = _ensure_float(value, name)
    if v < 0:
        raise ValueError(f"{name} darf nicht negativ sein")
    return v


# --- Stoffmenge ---
def mol_to_mmol(mol: float) -> float:
    return _ensure_non_negative(mol, "Stoffmenge (mol)") * 1000


def mmol_to_mol(mmol: float) -> float:
    return _ensure_non_negative(mmol, "Stoffmenge (mmol)") / 1000


def mol_to_umol(mol: float) -> float:
    return _ensure_non_negative(mol, "Stoffmenge (mol)") * 1_000_000


def umol_to_mol(umol: float) -> float:
    return _ensure_non_negative(umol, "Stoffmenge (µmol)") / 1_000_000


def mmol_to_umol(mmol: float) -> float:
    return _ensure_non_negative(mmol, "Stoffmenge (mmol)") * 1000


def umol_to_mmol(umol: float) -> float:
    return _ensure_non_negative(umol, "Stoffmenge (µmol)") / 1000


# --- Masse ---
def ug_to_mg(ug: float) -> float:
    return _ensure_non_negative(ug, "Masse (µg)") / 1000


def mg_to_ug(mg: float) -> float:
    return _ensure_non_negative(mg, "Masse (mg)") * 1000


def ug_to_g(ug: float) -> float:
    return _ensure_non_negative(ug, "Masse (µg)") / 1_000_000


def g_to_ug(g: float) -> float:
    return _ensure_non_negative(g, "Masse (g)") * 1_000_000


def ug_to_kg(ug: float) -> float:
    return _ensure_non_negative(ug, "Masse (µg)") / 1_000_000_000


def kg_to_ug(kg: float) -> float:
    return _ensure_non_negative(kg, "Masse (kg)") * 1_000_000_000


def ug_to_t(ug: float) -> float:
    return _ensure_non_negative(ug, "Masse (µg)") / 1_000_000_000_000


def t_to_ug(t: float) -> float:
    return _ensure_non_negative(t, "Masse (t)") * 1_000_000_000_000


def mg_to_g(mg: float) -> float:
    return _ensure_non_negative(mg, "Masse (mg)") / 1000


def g_to_mg(g: float) -> float:
    return _ensure_non_negative(g, "Masse (g)") * 1000


def mg_to_kg(mg: float) -> float:
    return _ensure_non_negative(mg, "Masse (mg)") / 1_000_000


def kg_to_mg(kg: float) -> float:
    return _ensure_non_negative(kg, "Masse (kg)") * 1_000_000


def mg_to_t(mg: float) -> float:
    return _ensure_non_negative(mg, "Masse (mg)") / 1_000_000_000


def t_to_mg(t: float) -> float:
    return _ensure_non_negative(t, "Masse (t)") * 1_000_000_000


def g_to_kg(g: float) -> float:
    return _ensure_non_negative(g, "Masse (g)") / 1000


def kg_to_g(kg: float) -> float:
    return _ensure_non_negative(kg, "Masse (kg)") * 1000


def g_to_t(g: float) -> float:
    return _ensure_non_negative(g, "Masse (g)") / 1_000_000


def t_to_g(t: float) -> float:
    return _ensure_non_negative(t, "Masse (t)") * 1_000_000


def kg_to_t(kg: float) -> float:
    return _ensure_non_negative(kg, "Masse (kg)") / 1000


def t_to_kg(t: float) -> float:
    return _ensure_non_negative(t, "Masse (t)") * 1000


# --- Volumen ---
def l_to_ml(l: float) -> float:
    return _ensure_non_negative(l, "Volumen (L)") * 1000


def ml_to_l(ml: float) -> float:
    return _ensure_non_negative(ml, "Volumen (mL)") / 1000


def l_to_cl(l: float) -> float:
    return _ensure_non_negative(l, "Volumen (L)") * 100


def cl_to_l(cl: float) -> float:
    return _ensure_non_negative(cl, "Volumen (cL)") / 100


def l_to_ul(l: float) -> float:
    return _ensure_non_negative(l, "Volumen (L)") * 1_000_000


def ul_to_l(ul: float) -> float:
    return _ensure_non_negative(ul, "Volumen (µL)") / 1_000_000


def ml_to_cl(ml: float) -> float:
    return _ensure_non_negative(ml, "Volumen (mL)") / 10


def cl_to_ml(cl: float) -> float:
    return _ensure_non_negative(cl, "Volumen (cL)") * 10


def ml_to_ul(ml: float) -> float:
    return _ensure_non_negative(ml, "Volumen (mL)") * 1000


def ul_to_ml(ul: float) -> float:
    return _ensure_non_negative(ul, "Volumen (µL)") / 1000


def cl_to_ul(cl: float) -> float:
    return _ensure_non_negative(cl, "Volumen (cL)") * 10000


def ul_to_cl(ul: float) -> float:
    return _ensure_non_negative(ul, "Volumen (µL)") / 10000


# --- Temperatur ---
def celsius_to_fahrenheit(c: float) -> float:
    c = _ensure_float(c, "Temperatur (°C)")
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    f = _ensure_float(f, "Temperatur (°F)")
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    c = _ensure_float(c, "Temperatur (°C)")
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    k = _ensure_float(k, "Temperatur (K)")
    return k - 273.15


def fahrenheit_to_kelvin(f: float) -> float:
    f = _ensure_float(f, "Temperatur (°F)")
    return (f - 32) * 5 / 9 + 273.15


def kelvin_to_fahrenheit(k: float) -> float:
    k = _ensure_float(k, "Temperatur (K)")
    return (k - 273.15) * 9 / 5 + 32


def calculate_conversion(value: float, from_unit: str, to_unit: str) -> dict:
    value = _ensure_float(value, "Wert")

    if from_unit == to_unit:
        result = value

    # Volumen
    elif from_unit == "L" and to_unit == "mL":
        result = l_to_ml(value)
    elif from_unit == "mL" and to_unit == "L":
        result = ml_to_l(value)
    elif from_unit == "L" and to_unit == "cL":
        result = l_to_cl(value)
    elif from_unit == "cL" and to_unit == "L":
        result = cl_to_l(value)
    elif from_unit == "L" and to_unit == "µL":
        result = l_to_ul(value)
    elif from_unit == "µL" and to_unit == "L":
        result = ul_to_l(value)
    elif from_unit == "mL" and to_unit == "cL":
        result = ml_to_cl(value)
    elif from_unit == "cL" and to_unit == "mL":
        result = cl_to_ml(value)
    elif from_unit == "mL" and to_unit == "µL":
        result = ml_to_ul(value)
    elif from_unit == "µL" and to_unit == "mL":
        result = ul_to_ml(value)
    elif from_unit == "cL" and to_unit == "µL":
        result = cl_to_ul(value)
    elif from_unit == "µL" and to_unit == "cL":
        result = ul_to_cl(value)

    # Masse
    elif from_unit == "µg" and to_unit == "mg":
        result = ug_to_mg(value)
    elif from_unit == "mg" and to_unit == "µg":
        result = mg_to_ug(value)
    elif from_unit == "µg" and to_unit == "g":
        result = ug_to_g(value)
    elif from_unit == "g" and to_unit == "µg":
        result = g_to_ug(value)
    elif from_unit == "µg" and to_unit == "kg":
        result = ug_to_kg(value)
    elif from_unit == "kg" and to_unit == "µg":
        result = kg_to_ug(value)
    elif from_unit == "µg" and to_unit == "t":
        result = ug_to_t(value)
    elif from_unit == "t" and to_unit == "µg":
        result = t_to_ug(value)
    elif from_unit == "mg" and to_unit == "g":
        result = mg_to_g(value)
    elif from_unit == "g" and to_unit == "mg":
        result = g_to_mg(value)
    elif from_unit == "mg" and to_unit == "kg":
        result = mg_to_kg(value)
    elif from_unit == "kg" and to_unit == "mg":
        result = kg_to_mg(value)
    elif from_unit == "mg" and to_unit == "t":
        result = mg_to_t(value)
    elif from_unit == "t" and to_unit == "mg":
        result = t_to_mg(value)
    elif from_unit == "g" and to_unit == "kg":
        result = g_to_kg(value)
    elif from_unit == "kg" and to_unit == "g":
        result = kg_to_g(value)
    elif from_unit == "g" and to_unit == "t":
        result = g_to_t(value)
    elif from_unit == "t" and to_unit == "g":
        result = t_to_g(value)
    elif from_unit == "kg" and to_unit == "t":
        result = kg_to_t(value)
    elif from_unit == "t" and to_unit == "kg":
        result = t_to_kg(value)

    # Stoffmenge
    elif from_unit == "mol" and to_unit == "mmol":
        result = mol_to_mmol(value)
    elif from_unit == "mmol" and to_unit == "mol":
        result = mmol_to_mol(value)
    elif from_unit == "mol" and to_unit == "µmol":
        result = mol_to_umol(value)
    elif from_unit == "µmol" and to_unit == "mol":
        result = umol_to_mol(value)
    elif from_unit == "mmol" and to_unit == "µmol":
        result = mmol_to_umol(value)
    elif from_unit == "µmol" and to_unit == "mmol":
        result = umol_to_mmol(value)

    # Temperatur
    elif from_unit == "°C" and to_unit == "°F":
        result = celsius_to_fahrenheit(value)
    elif from_unit == "°F" and to_unit == "°C":
        result = fahrenheit_to_celsius(value)
    elif from_unit == "°C" and to_unit == "K":
        result = celsius_to_kelvin(value)
    elif from_unit == "K" and to_unit == "°C":
        result = kelvin_to_celsius(value)
    elif from_unit == "°F" and to_unit == "K":
        result = fahrenheit_to_kelvin(value)
    elif from_unit == "K" and to_unit == "°F":
        result = kelvin_to_fahrenheit(value)

    else:
        raise ValueError("Diese Umrechnung wird nicht unterstützt")

    return {
        "timestamp": datetime.now(pytz.timezone("Europe/Zurich")),
        "Wert": value,
        "Von": from_unit,
        "Nach": to_unit,
        "Ergebnis": result,
    }
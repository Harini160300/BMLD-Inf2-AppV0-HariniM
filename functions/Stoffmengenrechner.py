def _ensure_number(value: Number, name: str) -> float:
    """Stellt sicher, dass value eine Zahl ist; gibt sie als float zurück."""
    if value is None:
        raise ValueError(f"{name} darf nicht None sein")
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} muss eine Zahl sein")


def _ensure_non_negative(value: Number, name: str) -> float:
    """Stellt sicher, dass value >= 0 ist."""
    v = _ensure_number(value, name)
    if v < 0:
        raise ValueError(f"{name} darf nicht negativ sein")
    return v


def _ensure_positive(value: Number, name: str) -> float:
    """Stellt sicher, dass value > 0 ist."""
    v = _ensure_number(value, name)
    if v <= 0:
        raise ValueError(f"{name} muss größer als 0 sein")
    return v


# --- Volumen ---
def l_to_ml(l: Number) -> float:
    """Liter -> Milliliter"""
    v = _ensure_non_negative(l, "Volumen (L)")
    return float(v) * 1000.0

def ml_to_l(ml: Number) -> float:
    """Milliliter -> Liter"""
    v = _ensure_non_negative(ml, "Volumen (mL)")
    return float(v) / 1000.0


def ml_to_ul(ml: Number) -> float:
    """Milliliter -> Mikroliter"""
    v = _ensure_non_negative(ml, "Volumen (mL)")
    return float(v) * 1000.0


def ul_to_ml(ul: Number) -> float:
    """Mikroliter -> Milliliter"""
    v = _ensure_non_negative(ul, "Volumen (µL)")
    return float(v) / 1000.0

# --- Masse ---
def mg_to_g(mg: Number) -> float:
    """Milligramm -> Gramm"""
    v = _ensure_non_negative(mg, "Masse (mg)")
    return float(v) / 1000.0


def g_to_mg(g: Number) -> float:
    """Gramm -> Milligramm"""
    v = _ensure_non_negative(g, "Masse (g)")
    return float(v) * 1000.0


def g_to_kg(g: Number) -> float:
    """Gramm -> Kilogramm"""
    v = _ensure_non_negative(g, "Masse (g)")
    return float(v) / 1000.0


def kg_to_g(kg: Number) -> float:
    """Kilogramm -> Gramm"""
    v = _ensure_non_negative(kg, "Masse (kg)")
    return float(v) * 1000.0


def kg_to_tonne(kg: Number) -> float:
    """Kilogramm -> Tonne (metrisch)"""
    v = _ensure_non_negative(kg, "Masse (kg)")
    return float(v) / 1000.0


def tonne_to_kg(tonne: Number) -> float:
    """Tonne -> Kilogramm"""
    v = _ensure_non_negative(tonne, "Masse (t)")
    return float(v) * 1000.0

def ug_to_mg(ug: Number) -> float:
    """Mikrogramm -> Milligramm"""
    v = _ensure_non_negative(ug, "Masse (µg)")
    return float(v) / 1000.0


def mg_to_ug(mg: Number) -> float:
    """Milligramm -> Mikrogramm"""
    v = _ensure_non_negative(mg, "Masse (mg)")
    return float(v) * 1000.0


# --- Stoffmengen ---
def mol_to_mmol(mol: Number) -> float:
    """Mol -> Millimol"""
    v = _ensure_non_negative(mol, "Stoffmenge (mol)")
    return float(v) * 1000.0


def mmol_to_mol(mmol: Number) -> float:
    """Millimol -> Mol"""
    v = _ensure_non_negative(mmol, "Stoffmenge (mmol)")
    return float(v) / 1000.0


def mol_to_micromol(mol: Number) -> float:
    """Mol -> Mikromol (µmol)"""
    v = _ensure_non_negative(mol, "Stoffmenge (mol)")
    return float(v) * 1_000_000.0


def micromol_to_mol(umol: Number) -> float:
    """Mikromol (µmol) -> Mol"""
    v = _ensure_non_negative(umol, "Stoffmenge (µmol)")
    return float(v) / 1_000_000.0

# --- Temperatur ---
def celsius_to_fahrenheit(c: Number) -> float:
    """Celsius -> Fahrenheit"""
    v = _ensure_number(c, "Temperatur (°C)")
    return (v * 9.0 / 5.0) + 32.0


def fahrenheit_to_celsius(f: Number) -> float:
    """Fahrenheit -> Celsius"""
    v = _ensure_number(f, "Temperatur (°F)")
    return (v - 32.0) * 5.0 / 9.0


def celsius_to_kelvin(c: Number) -> float:
    """Celsius -> Kelvin"""
    v = _ensure_number(c, "Temperatur (°C)")
    k = v + 273.15
    if k < 0:
        # physikalisch unmöglich, Abfangen (wird selten eintreten, da v float)
        raise ValueError("Resultierende Kelvin-Temperatur ist negativ (physikalisch unmöglich)")
    return k


def kelvin_to_celsius(k: Number) -> float:
    """Kelvin -> Celsius"""
    v = _ensure_number(k, "Temperatur (K)")
    if v < 0:
        raise ValueError("Temperatur (K) darf nicht negativ sein")
    return v - 273.15


# --- Utility ---
def format_number(value: Number, sig_digits: int = 6) -> str:
    """Einfacher Format-Helper (wissenschaftliche Notation bei Bedarf)."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        return str(value)
    return f"{v:.{sig_digits}g}"
# ...existing code...
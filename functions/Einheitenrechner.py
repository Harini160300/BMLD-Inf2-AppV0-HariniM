# functions/Einheitenrechner.py

def _ensure_float(value: float, name: str) -> float:
    """Stellt sicher, dass value eine Zahl ist; gibt sie als float zurück."""
    if value is None:
        raise ValueError(f"{name} darf nicht None sein")
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} muss eine Zahl sein")


def _ensure_non_negative(value: float, name: str) -> float:
    """Stellt sicher, dass value >= 0 ist."""
    v = _ensure_float(value, name)
    if v < 0:
        raise ValueError(f"{name} darf nicht negativ sein")
    return v


# --- Stoffmenge Kombinationen ---

def mol_to_mmol(mol: float) -> float:
    return mol * 1000

def mmol_to_mol(mmol: float) -> float:
    return mmol / 1000

def mol_to_umol(mol: float) -> float:
    return mol * 1_000_000

def umol_to_mol(umol: float) -> float:
    return umol / 1_000_000

def mmol_to_umol(mmol: float) -> float:
    return mmol * 1000

def umol_to_mmol(umol: float) -> float:
    return umol / 1000


# --- Masse Kombinationen ---

def ug_to_mg(ug): return ug / 1000
def mg_to_ug(mg): return mg * 1000

def ug_to_g(ug): return ug / 1_000_000
def g_to_ug(g): return g * 1_000_000

def ug_to_kg(ug): return ug / 1_000_000_000
def kg_to_ug(kg): return kg * 1_000_000_000

def ug_to_t(ug): return ug / 1_000_000_000_000
def t_to_ug(t): return t * 1_000_000_000_000

def mg_to_g(mg): return mg / 1000
def g_to_mg(g): return g * 1000

def mg_to_kg(mg): return mg / 1_000_000
def kg_to_mg(kg): return kg * 1_000_000

def mg_to_t(mg): return mg / 1_000_000_000
def t_to_mg(t): return t * 1_000_000_000

def g_to_kg(g): return g / 1000
def kg_to_g(kg): return kg * 1000

def g_to_t(g): return g / 1_000_000
def t_to_g(t): return t * 1_000_000

def kg_to_t(kg): return kg / 1000
def t_to_kg(t): return t * 1000



# --- Volumen Kombinationen ---

def l_to_ml(l): return l * 1000
def ml_to_l(ml): return ml / 1000

def l_to_cl(l): return l * 100
def cl_to_l(cl): return cl / 100

def l_to_ul(l): return l * 1_000_000
def ul_to_l(ul): return ul / 1_000_000

def ml_to_cl(ml): return ml / 10
def cl_to_ml(cl): return cl * 10

def ml_to_ul(ml): return ml * 1000
def ul_to_ml(ul): return ul / 1000

def cl_to_ul(cl): return cl * 10000
def ul_to_cl(ul): return ul / 10000


# --- Temperatur Kombinationen ---

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# --- Utility ---
def format_float(value: float, sig_digits: int = 6) -> str:
    """Einfacher Format-Helper."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        return str(value)
    return f"{v:.{sig_digits}g}"
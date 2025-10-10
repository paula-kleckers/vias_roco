# Listado de rocódromos, tipo de vía y dificultades asociadas a las mismas
opciones = {
    "": {"": [""]},
    "One Move": {
        "": [""],
        "Boulder": ["", "🩵 Turquesa", "🟩 Verde", "🟨 Amarilla", "⬜ Blanca", "🟦 Azul", "🟥 Roja", "⬛ Negra"],
        "Cuerda": ["", "🟩 Verde", "🟨 Amarilla", "🟦 Azul", "🟥 Roja"],
        "Stokt": ["", "4a", "4b", "4c", "5a", "5b", "5c", "6a", "6a+", "6b", "6b+", "6c", "6c+", "7a", "7a+", "7b",
                  "7b+", "7c", "7c+", "8a", "8a+", "8b", "8b+", "8c", "8c+"],
        "Kilter": ["", "4a", "4b", "4c", "5a", "5b", "5c", "6a", "6a+", "6b", "6b+", "6c", "6c+", "7a", "7a+", "7b",
                   "7b+", "7c", "7c+", "8a", "8a+", "8b", "8b+", "8c", "8c+"],
    },
    "Climbat": {
        "": [""],
        "Boulder": ["", "⬜ Blanca", "🟨 Amarilla", "🟧 Naranja", "🟩 Verde", "🟦 Azul", "🟥 Roja", "⬛ Negra"],
        "Cuerda": ["", "4", "4+", "5", "5+", "6a", "6a+", "6b", "6b+", "6c", "6c+", "7a", "7a+", "7b", "7b+", "7c",
                   "7c+"],
    },
    "Mata Jove": {
        "": [""],
        "Cuerda": ["", "4", "4+", "5", "5+", "6a", "6a+", "6b", "6b+", "6c", "6c+", "7a", "7a+", "7b", "7b+", "7c",
                   "7c+"],
    },
    "El RoKo": {
        "": [""],
        "Boulder": ["", "🟩 Verde", "🟨 Amarilla", "🟧 Naranja", "🌸 Rosa", "🟪 Morada", "⬛ Negra"],
        "Cuerda": ["Pendiente de añadir", "4", "4+", "5", "5+", "6a", "6a+", "6b", "6b+", "6c", "6c+", "7a", "7a+",
                   "7b", "7b+", "7c", "7c+"],
        "Kilter": ["", "4a", "4b", "4c", "5a", "5b", "5c", "6a", "6a+", "6b", "6b+", "6c", "6c+", "7a", "7a+", "7b",
                   "7b+", "7c", "7c+", "8a", "8a+", "8b", "8b+", "8c", "8c+"],
    },
    "Adamanta Gonzalitos": {
        "": [""],
        "Boulder": ["", "V0", "V1", "V2", "V3", "V3+", "V4", "V4+", "V5", "V5+", "V6", "V6+", "V7", "V7+", "V8", "V8+",
                    "V9", "V9+"],
        "Cuerda": ["", "V0", "V1", "V2", "V3", "V3+", "V4", "V4+", "V5", "V5+", "V6", "V6+", "V7", "V7+", "V8", "V8+",
                   "V9", "V9+"],
    },
}

# Dificultad estándar definida para Boulder (se ha seguido el convenio correpsondiente al Climbat)
dificultad_estandar_boulder = ["⬜ Blanca", "🟨 Amarilla", "🟧 Naranja", "🟩 Verde", "🟦 Azul", "🟥 Roja", "⬛ Negra"]

# Mapeo de equivalencias de dificultad entre los diferentes rocódromos
dificultad_eq_color_estandar = {
    "One Move": {
        "🩵 Turquesa": dificultad_estandar_boulder[0],
        "🟩 Verde": dificultad_estandar_boulder[1],
        "🟨 Amarilla": dificultad_estandar_boulder[2],
        "⬜ Blanca": dificultad_estandar_boulder[3],
        "🟦 Azul": dificultad_estandar_boulder[4],
        "🟥 Roja": dificultad_estandar_boulder[5],
        "⬛ Negra": dificultad_estandar_boulder[6],
    },
    "Climbat": {
        "⬜ Blanca": dificultad_estandar_boulder[0],
        "🟨 Amarilla": dificultad_estandar_boulder[1],
        "🟧 Naranja": dificultad_estandar_boulder[2],
        "🟩 Verde": dificultad_estandar_boulder[3],
        "🟦 Azul": dificultad_estandar_boulder[4],
        "🟥 Roja": dificultad_estandar_boulder[5],
        "⬛ Negra": dificultad_estandar_boulder[6],
    },
    "El RoKo": {
        "🟩 Verde": dificultad_estandar_boulder[0],   # Verde -> Blanca
        "🟨 Amarilla": dificultad_estandar_boulder[1], # Amarilla -> Amarilla
        "🟧 Naranja": dificultad_estandar_boulder[3],  # Naranja -> Verde
        "🌸 Rosa": dificultad_estandar_boulder[4],     # Rosa -> Azul
        "🟪 Morada": dificultad_estandar_boulder[5],   # Morada -> Roja
        "⬛ Negra": dificultad_estandar_boulder[6],    # Negra -> Negra
    },
}

# Equivalencias entre los colores estándar establecidos y las dificultades por escala francesa
# (se ha seguido aproximadamente la clasificación de boulder del Climbat, aunque está abierta a modificaciones)
dificultad_eq_estandar_font = {
    dificultad_estandar_boulder[0]: ["4a", "4b", "4c"],
    dificultad_estandar_boulder[1]: ["5a", "5b"],
    dificultad_estandar_boulder[2]: ["5c", "6a"],
    dificultad_estandar_boulder[3]: ["6a+", "6b"],
    dificultad_estandar_boulder[4]: ["6b+", "6c"],
    dificultad_estandar_boulder[5]: ["6c+", "7a", "7a+"],
    dificultad_estandar_boulder[6]: ["7b", "7b+", "7c"]
}

# Equivalencias entre los colores estándar establecidos y las dificultades por v-scale
# (se ha seguido un criterio por sensaciones, aunque está abierta a modificaciones)
dificultad_eq_estandar_vscale = {
    dificultad_estandar_boulder[0]: ["V0"],
    dificultad_estandar_boulder[1]: ["V1"],
    dificultad_estandar_boulder[2]: ["V2", "V3"],
    dificultad_estandar_boulder[3]: ["V3+", "V4"],
    dificultad_estandar_boulder[4]: ["V4+", "V5"],
    dificultad_estandar_boulder[5]: ["V5+", "V6", "V6+"],
    dificultad_estandar_boulder[6]: ["V7", "V7+", "V8"]
}

# FUNCIONES DE EQUIVALENCIA PARA LAS VISUALIZACIONES (BOULDER)

# 1. Convertir color de rocódromo al color estándar
def convertir_color_rocodromo_a_estandar(rocodromo: str, color: str) -> str | None:
    """
    Convierte un color de un rocódromo (One Move o Climbat) al color estándar.
    """
    mapa = dificultad_eq_color_estandar.get(rocodromo)
    if not mapa:
        raise ValueError(f"Rocódromo no reconocido: {rocodromo}")
    return mapa.get(color)

# 2. Convertir grado V-scale al color estándar
def convertir_vscale_a_color_estandar(vscale: str) -> str | None:
    """
    Convierte un grado V-scale al color estándar correspondiente.
    """
    for color, grados in dificultad_eq_estandar_vscale.items():
        if vscale in grados:
            return color
    return None

# 3. Convertir grado Fontainebleau al color estándar
def convertir_fontainebleau_a_color_estandar(grado_font: str) -> str | None:
    """
    Convierte un grado Fontainebleau (ej. '6b+') al color estándar correspondiente.
    """
    for color, grados in dificultad_eq_estandar_font.items():
        if grado_font in grados:
            return color
    return None

# Convertir dificultad oficial a dificultad estándar
def obtener_color_estandar(row):
    rocodromo = row.get("rocodromo", "").strip()
    dificultad_oficial = row.get("dificultad_oficial", "").strip()

    # NOTA: Depende del rocódromo!!!!
    if rocodromo in ["Climbat", "One Move", "El RoKo"]:
        return convertir_color_rocodromo_a_estandar(rocodromo, dificultad_oficial)
    elif rocodromo == "Adamanta Gonzalitos":
        return convertir_vscale_a_color_estandar(dificultad_oficial)
    else:
        return convertir_fontainebleau_a_color_estandar(dificultad_oficial)


# -------------------------------------------------------------------------------------------------------------------

# Equivalencias de dificultad oficial en base a la clasificación de la app de Kilter Board
dificultad_eq_vscale_font = {"V0": ["4a", "4b", "4c"],
                             "V1": ["5a", "5b"],
                             "V2": ["5c"],
                             "V3": ["6a"],
                             "V3+": ["6a+"],
                             "V4": ["6b"],
                             "V4+": ["6b+"],
                             "V5": ["6c"],
                             "V5+": ["6c+"],
                             "V6": ["7a"],
                             "V6+": ["7a+"],
                             "V7": ["7b"],
                             "V7+": ["7b+"],
                             "V8": ["7c"],
                             "V8+": ["7c+"],
                             "V9": ["8a"],
                             "V9+": ["8a+"],
                             }

# FUNCIONES DE EQUIVALENCIA PARA VISUALIZACIONES (CUERDA)

def vscale_to_font_custom_vscale(vscale_grade: str) -> str:
    vscale_grade = vscale_grade.strip().upper()
    if vscale_grade == "V0":
        return "4b"
    elif vscale_grade == "V1":
        return "5b"
    elif vscale_grade in dificultad_eq_vscale_font:
        return dificultad_eq_vscale_font[vscale_grade][0]
    else:
        return "?"  # Valor desconocido

# Función auxiliar que convierte solo si el grado está en V-scale
def convertir_si_vscale(grade):
    grade = grade.strip()
    if grade.startswith("V"):
        return vscale_to_font_custom_vscale(grade)
    else:
        return grade  # Deja el valor original si no es V-scale


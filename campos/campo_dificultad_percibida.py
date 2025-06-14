import streamlit as st

def input_dificultad_percibida(dificultad_oficial, opciones):
    opciones_finales = []

    for d in opciones:
        if d == dificultad_oficial:
            opciones_finales.extend([
                f"{d} (más fácil)",
                f"{d}",
                f"{d} (más difícil)"
            ])
        else:
            opciones_finales.append(d)

    # Insertar valor por defecto vacío
    opciones_finales.insert(0, "")

    return st.selectbox("Dificultad percibida", opciones_finales, key="dificultad_percibida",
                        help="Selecciona la dificultad que crees que debería de ser asignada a la vía.\n"
                             "Puedes seleccionar la dificultad oficial, devaluar o sobrevalorar la vía.\n"
                             "Si crees que la vía está bien valorada pero es más fácil o más difícil de lo que suelen "
                             "ser las vías de ese nivel habitualmente, indícalo.\n"
                             "NOTA: Si se muestran los valores vacíos, comprueba haber seleccionado una dificultad "
                             "oficial.")

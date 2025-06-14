import streamlit as st
from campos.seleccion_roco_tipo_dif import opciones

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

    return st.selectbox("Dificultad percibida", opciones_finales, key="dificultad_percibida")

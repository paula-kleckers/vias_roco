import streamlit as st
from campos.seleccion_roco_tipo_dif import opciones

def input_rocodromo():
    rocodromos = list(opciones.keys())
    valor_actual = st.session_state.get("rocodromo", rocodromos[0])
    index = rocodromos.index(valor_actual) if valor_actual in rocodromos else 0
    return st.selectbox(
        "Rocódromo",
        rocodromos,
        index=index,
        key="rocodromo",
        help="Selecciona el rocódromo al que pertenece la vía"
    )
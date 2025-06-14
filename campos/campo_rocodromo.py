import streamlit as st
from campos.seleccion_roco_tipo_dif import opciones

def input_rocodromo():
    rocodromos = list(opciones.keys())
    return st.selectbox("Rocódromo", rocodromos, index=0, key="rocodromo",
                        help="Selecciona el rocódromo al que pertenece la vía")

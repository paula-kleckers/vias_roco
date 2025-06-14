import streamlit as st
from campos.seleccion_roco_tipo_dif import opciones

def input_rocodromo():
    rocodromos = list(opciones.keys())
    return st.selectbox("Rocódromo", rocodromos, key="rocodromo")

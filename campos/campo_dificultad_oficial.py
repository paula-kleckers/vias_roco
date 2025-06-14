import streamlit as st
from campos.seleccion_roco_tipo_dif import opciones

def input_dificultad_oficial(rocodromo, tipo_via):
    dificultades = opciones[rocodromo][tipo_via]
    seleccion = st.selectbox("Dificultad oficial", dificultades, key="dificultad")
    return seleccion, dificultades

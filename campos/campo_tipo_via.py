import streamlit as st

def input_tipo_via():
    opciones = ["Boulder", "Cuerda"]
    tipo = st.radio("Tipo de vía", opciones, horizontal=True)
    return tipo
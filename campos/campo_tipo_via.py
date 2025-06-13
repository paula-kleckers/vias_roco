import streamlit as st

def input_tipo_via():
    opciones = ["Deportiva", "Bloque", "Clásica", "Alpina", "Mixta", "Otro"]
    return st.selectbox("Tipo de vía", opciones)

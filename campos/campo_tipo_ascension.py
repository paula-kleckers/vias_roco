import streamlit as st

def input_tipo_ascension():
    opciones = ["Flash", "A vista", "Entrenamiento", "Trabajo", "Otro"]
    return st.selectbox("Tipo de ascensión", opciones)

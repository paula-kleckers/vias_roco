import streamlit as st
import pandas as pd
import os

DATA_FILE = "data.csv"

def cargar_nombres():
    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)
            return sorted(df["Escalador"].dropna().unique().tolist())
        except:
            return []
    else:
        return []

def input_escalador():
    nombres = cargar_nombres()

    tab_nuevo, tab_existente = st.tabs(["Nuevo", "Existente"])

    with tab_nuevo:
        nombre_nuevo = st.text_input("Introduce el nombre del nuevo escalador")

    with tab_existente:
        if nombres:
            nombre_existente = st.selectbox("Selecciona un escalador existente", nombres)
        else:
            st.info("No hay escaladores registrados aún.")
            nombre_existente = None

    # Priorizar el nombre nuevo si se ha escrito, si no, el existente
    nombre_final = nombre_nuevo.strip() if nombre_nuevo.strip() else nombre_existente

    return nombre_final


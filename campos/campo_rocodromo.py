import streamlit as st
import pandas as pd
import os

DATA_FILE = "data.csv"

def cargar_rocodromos():
    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)
            return sorted(df["Rocódromo"].dropna().unique().tolist())
        except:
            return []
    else:
        return []

def input_rocodromo():
    rocodromos = cargar_rocodromos()

    tab_nuevo, tab_existente = st.tabs(["Nuevo", "Existente"])

    with tab_nuevo:
        rocodromo_nuevo = st.text_input("Introduce el nombre del nuevo rocódromo")

    with tab_existente:
        if rocodromos:
            rocodromo_existente = st.selectbox("Selecciona un rocódromo existente", rocodromos)
        else:
            st.info("No hay rocódromos registrados aún.")
            rocodromo_existente = None

    # Priorizar el rocódromo nuevo si se ha escrito, si no, el existente
    rocodromo_final = rocodromo_nuevo.strip() if rocodromo_nuevo.strip() else rocodromo_existente

    return rocodromo_final
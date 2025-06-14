import streamlit as st

def input_escalador(df):
    st.header("Escalador")

    # Checkbox para elegir si es nuevo o no
    es_nuevo = st.checkbox("¿Nuevo escalador?", value=False)

    if es_nuevo:
        nombre = st.text_input("Introduce el nombre del nuevo escalador")
    else:
        # Lista de escaladores registrados
        escaladores_existentes = (
            df["Escalador"].dropna().astype(str).unique().tolist()
        )
        escaladores_existentes = sorted(escaladores_existentes)

        nombre = st.selectbox("Selecciona un escalador", escaladores_existentes)

    return nombre.strip()

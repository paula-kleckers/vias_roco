import streamlit as st

def input_escalador(df):
    st.header("Escalador")

    # Checkbox para elegir si es nuevo o no
    es_nuevo = st.checkbox("Nuevo escalador", value=False)

    if es_nuevo:
        nombre = st.text_input("Introduce el nombre del nuevo escalador")
    else:
        # Lista de escaladores registrados
        escaladores_existentes = (
            df["escalador"].dropna().astype(str).unique().tolist()
        )
        escaladores_existentes = sorted(escaladores_existentes)
        escaladores_existentes = [""] + escaladores_existentes

        nombre = st.selectbox("Selecciona un escalador", escaladores_existentes,
                              help="Selecciona un escalador registrado. Si no está, selecciona Nuevo escalador e "
                                   "introduce el nombre")

    return nombre.strip()

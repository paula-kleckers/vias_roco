import streamlit as st

def input_indice(df):
    # Mostrar índice como entero, empezando en 0 (coincidiendo con df.index)
    if "indice_registro" not in st.session_state:
        st.session_state.indice_registro = len(df)

    indice_indicado = st.number_input(
        "Índice del registro (0 = primera fila, {} = nuevo)".format(len(df)),
        min_value=0,
        max_value=max(len(df), 0),
        value=st.session_state.indice_registro,
        step=1,
        key="indice_registro_input"
    )
    if indice_indicado < len(df):
        st.warning(f"⚠️ Vas a sobrescribir la fila existente #{indice_indicado}")

    return indice_indicado

def reset_indice(df):
    st.session_state.indice_registro = len(df)

import streamlit as st

def input_escalador(df):
    st.header("Escalador")

    # Checkbox para elegir si es nuevo o no
    es_nuevo = st.checkbox(
        "Nuevo escalador",
        value=st.session_state.get("es_nuevo_escalador", False),
        key="es_nuevo_escalador"
    )

    if es_nuevo:
        st.text_input(
            "Introduce el nombre del nuevo escalador",
            value=st.session_state.get("nombre_escalador", ""),
            key="nombre_escalador"
        )
    else:
        escaladores_existentes = sorted(
            df["escalador"].dropna().astype(str).unique().tolist()) if "escalador" in df.columns else []
        escaladores_existentes = [""] + escaladores_existentes

        st.selectbox(
            "Selecciona un escalador",
            escaladores_existentes,
            index=escaladores_existentes.index(st.session_state.get("nombre_escalador", ""))
            if st.session_state.get("nombre_escalador", "") in escaladores_existentes else 0,
            key="nombre_escalador"
        )

    return st.session_state.nombre_escalador.strip()

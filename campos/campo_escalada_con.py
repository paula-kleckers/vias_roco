import streamlit as st

def input_escalada_con(df, escalador_seleccionado):

    escalada_con_existente = escalada_con_existentes(df, escalador_seleccionado)
    escalada_con_nuevo = escalada_con_nuevos()
    escalada_con = escalada_con_existente + escalada_con_nuevo
    escalada_con_str = ", ".join(escalada_con)
    return escalada_con_str

def escalada_con_existentes(df, escalador_seleccionado):
    # Multiselectbox de compañeros de escalada registrados

    st.header("Escalada con...")

    if "escalada_con_existente" not in st.session_state:
        st.session_state.escalada_con_existente = []

    # Extraer sugerencias como antes, desde el DataFrame actual
    escaladores = df["escalador"].dropna().unique().tolist() if "escalador" in df.columns else []

    if "escalada_con" in df.columns and df["escalada_con"].notna().any():
        escalada_con_existentes = (
            df["escalada_con"]
            .dropna()
            .astype(str)
            .str.split(",")
            .explode()
            .str.strip()
            .unique()
            .tolist()
        )
    else:
        escalada_con_existentes = []

    listado = sorted(set(escaladores + escalada_con_existentes))
    listado = [nombre for nombre in listado if nombre != escalador_seleccionado]

    st.multiselect(
        "Escalada con...",
        options=listado,
        default=st.session_state.escalada_con_existente,
        key="escalada_con_existente",
        help="Selecciona compañeros. Si no están, añádelos en la caja de texto de abajo"
    )

    return st.session_state.escalada_con_existente


def escalada_con_nuevos():
    if "companeros" not in st.session_state:
        st.session_state.companeros = []

    st.write("Añadir compañeros de escalada nuevos:")

    for i in range(len(st.session_state.companeros)):
        cols = st.columns([4,1])
        with cols[0]:
            st.session_state.companeros[i] = st.text_input(
                f"Compañero #{i+1}",
                value=st.session_state.companeros[i],
                key=f"comp_{i}"
            )
        with cols[1]:
            st.button(
                "🗑️",
                key=f"del_{i}",
                on_click=borrar_companero,
                args=(i,)
            )

    st.button("Añadir compañero", on_click=anadir_companero)

    # Filtrar nombres vacíos o solo espacios
    escalada_con_nuevos_filtrado = [c.strip() for c in st.session_state.companeros if c.strip() != ""]

    return escalada_con_nuevos_filtrado

def borrar_companero(indice):
    st.session_state.companeros.pop(indice)

def anadir_companero():
    st.session_state.companeros.append("")

import streamlit as st

def input_escalada_con(df, escalador_seleccionado):

    escalada_con_existente = escalada_con_existentes(df, escalador_seleccionado)
    escalada_con_nuevo = escalada_con_nuevos()
    escalada_con = escalada_con_existente + escalada_con_nuevo
    escalada_con_str = ", ".join(escalada_con)
    return escalada_con_str

def escalada_con_existentes(df, escalador_seleccionado):
    # Multiselectbox de compañeros de escalda registrados

    st.header("Escalada con...")

    # Extraer sugerencias como antes, desde el DataFrame actual
    escaladores = df["Escalador"].dropna().unique().tolist()

    escalada_con_existentes = (
        df["Escalada con..."]
        .dropna()
        .astype(str)
        .str.split(",")
        .explode()
        .str.strip()
        .unique()
        .tolist()
    )

    listado = sorted(set(escaladores + escalada_con_existentes))
    listado = [nombre for nombre in listado if nombre != escalador_seleccionado]

    escalada_con_existente = st.multiselect(
        "Escalada con...",
        options=listado,
        help="Selecciona compañeros. Si no están, añádelos en la cajas de texto de abajo",
        default=[]
    )

    return escalada_con_existente


def escalada_con_nuevos():
    # Si los compañeros no están en la lista, se añaden como cajas de texto

    if "companeros" not in st.session_state:
        st.session_state.companeros = [""]

    st.text("Añadir compañeros de escalada nuevos: ")

    # Mostrar cajas para cada compañero
    for i in range(1, len(st.session_state.companeros)):
        st.session_state.companeros[i] = st.text_input(
            f"Compañero #{i}",
            value=st.session_state.companeros[i],
            key=f"comp_{i}"
        )

    st.button("Añadir compañero", on_click=agregar_caja)

    # Limpiar nombres vacíos o solo espacios
    escalada_con_nuevos_filtrado = [c.strip() for c in st.session_state.companeros if c.strip() != ""]

    return escalada_con_nuevos_filtrado

def agregar_caja():
    st.session_state.companeros.append("")

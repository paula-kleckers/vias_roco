import streamlit as st
from datetime import date

def input_fecha():

    if "fecha" not in st.session_state:
        st.session_state["fecha"] = date.today()

    fecha_seleccionada = st.date_input(
        "Fecha",
        value=st.session_state["fecha"],
        help="Selecciona la fecha en que escalaste la vía"
    )
    st.session_state["fecha"] = fecha_seleccionada

    return fecha_seleccionada


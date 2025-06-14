import streamlit as st

def input_fecha():
    return st.date_input("Fecha", help="Selecciona la fecha en que escalaste la vía")

import streamlit as st

def input_intentos():
    return st.number_input("Intentos (en la fecha)", min_value=1, max_value=100, step=1)

import streamlit as st
from campos.seleccion_roco_tipo_dif import opciones

def input_tipo_via(rocodromo):
    tipos = list(opciones[rocodromo].keys())
    return st.selectbox("Tipo de vía", tipos, key="tipo_via",
                        help="Selecciona el tipo de vía. Puede ser Boulder o Cuerda.\n"
                             "NOTA: Si se muestran los valores vacíos, comprueba haber seleccionado un rocódromo.")

import streamlit as st
from campos.seleccion_roco_tipo_dif import opciones

def input_dificultad_oficial(rocodromo, tipo_via):
    dificultades = opciones[rocodromo][tipo_via]
    seleccion = st.selectbox("Dificultad oficial", dificultades, key="dificultad",
                             help="Selecciona la dificultad que el rocódromo ha asignado a la vía.\n"
                                  "NOTA: Si se muestran los valores vacíos, comprueba haber seleccionado un "
                                  "tipo de vía.")
    return seleccion, dificultades

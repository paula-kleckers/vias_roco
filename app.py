import streamlit as st
import pandas as pd
import os

from campos.campo_escalador import input_escalador
from campos.campo_nombre_via import input_nombre_via
from campos.campo_rocodromo import input_rocodromo
from campos.campo_tipo_via import input_tipo_via
from campos.campo_dificultad_oficial import input_dificultad_oficial
from campos.campo_fecha import input_fecha
from campos.campo_tipo_ascension import input_tipo_ascension
from campos.campo_intentos import input_intentos
from campos.campo_dificultad_percibida import input_dificultad_percibida
from campos.campo_valoracion import input_valoracion
from campos.campo_escalada_con import input_escalada_con
from campos.campo_comentarios_personales import input_comentarios_personales
from campos.campo_comentarios_tipo_ascension import input_comentarios_tipo_ascension


# ---------- CONFIGURACIÓN INICIAL ----------
st.set_page_config(page_title="Formulario y Análisis", layout="wide")

DATA_FILE = "data.csv"

# Cargar datos si existen
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["Escalador", "Nombre vía", "Rocódromo", "Tipo de vía", "Dificultad oficial", "Fecha",
                               "Tipo de ascensión", "Intentos (en la fecha)", "Dificultad percibida", "Valoración",
                               "Escalada con...", "Comentarios (personales)", "Comentarios (tipo de ascensión)"])

# ---------- FORMULARIO ----------
with st.sidebar:
    st.header("Agregar nuevo registro")
    with st.form(key="formulario_usuario"):
        escalador = input_escalador()
        nombre_via = input_nombre_via()
        rocódromo = input_rocodromo()
        tipo_via = input_tipo_via()
        dificultad_oficial = input_dificultad_oficial()
        fecha = input_fecha()
        tipo_ascension = input_tipo_ascension()
        intentos = input_intentos()
        dificultad_percibida = input_dificultad_percibida()
        valoracion = input_valoracion()
        escalada_con = input_escalada_con()
        comentarios_personales = input_comentarios_personales()
        comentarios_tipo_ascension = input_comentarios_tipo_ascension()

        submit_button = st.form_submit_button("Guardar")

    if submit_button:
        nuevo_registro = {
            "Escalador": escalador,
            "Nombre vía": nombre_via,
            "Rocódromo": rocódromo,
            "Tipo de vía": tipo_via,
            "Dificultad oficial": dificultad_oficial,
            "Fecha": fecha,
            "Tipo de ascensión": tipo_ascension,
            "Intentos (en la fecha)": intentos,
            "Dificultad percibida": dificultad_percibida,
            "Valoración": valoracion,
            "Escalada con...": escalada_con,
            "Comentarios (personales)": comentarios_personales,
            "Comentarios (tipo de ascensión)": comentarios_tipo_ascension
        }
        df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
        df.to_csv(DATA_FILE, index=False)
        st.success("Registro guardado correctamente")

st.header("📋 Datos recogidos")
st.dataframe(df, use_container_width=True)

# ---------- PESTAÑAS ----------
tab1, tab2 = st.tabs(["📋 Tabla de datos", "📊 Gráficos"])

with tab1:
    st.header("📋 Datos recogidos")
    st.dataframe(df, use_container_width=True)

# with tab2:
#     st.header("📊 Visualización de datos")
#     col1, col2 = st.columns(2)
#
#     with col1:
#         st.subheader("Distribución por edad")
#         st.bar_chart(df["Edad"].value_counts().sort_index())
#
#     with col2:
#         st.subheader("Nivel de satisfacción")
#         st.bar_chart(df["Satisfacción"].value_counts().sort_index())
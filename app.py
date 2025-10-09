import streamlit as st
import pandas as pd
import os
from supabase import create_client, Client

from campos.campo_indice import input_indice
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
from campos.campo_foto import input_foto

from charts.chart_dificultad_escalada import n_vias_escaladas_por_dificultad_y_escalador
from charts.chart_evolucion_dificultad_boulder_tiempo import *
from charts.chart_evolucion_dificultad_cuerda_tiempo import *

import utils as u

# ---------- CONFIGURACIÓN INICIAL ----------
st.set_page_config(page_title="Roco Climber", layout="wide")

def load_data():
    """Función para cargar datos desde Supabase"""
    try:
        response = supabase.table("climbing_data").select("*").order("fecha").execute()
        return pd.DataFrame(response.data)
    except Exception as e:
        st.error(f"Error al cargar los datos desde Supabase: {str(e)}")
        return pd.DataFrame(columns=[
            "escalador", "escalada_con", "fecha", "rocodromo", "tipo_via", "dificultad_oficial",
            "tipo_ascension", "intentos", "dificultad_percibida", "valoracion",
            "comentarios_personales", "comentarios_tipo_ascension", "nombre_via", "ruta_imagen"
        ])

# Tus credenciales de Supabase
url = "https://ubnslrintcfolygbnqsb.supabase.co"
with open("client_id/supabase_key.txt", "r") as f:
    key = f.read().strip()
supabase: Client = create_client(url, key)

with open("client_id/client_id.txt", "r") as f:
    CLIENT_ID = f.read().strip()

# Cargar datos
df = load_data()


# ---------- FORMULARIO ----------
with st.sidebar:
    st.header("Índice de fila para el registro")
    st.text("Si el índice corresponde con una fila existente, esta fila se actualizará con la nueva información")
    indice = input_indice(df)
    st.markdown("---")

    # 📌 Aquí llamas a la función para precargar valores
    u.cargar_valores_indice(df, indice)

    # Se agregan registros fuera de un formulario para garantizar que son dinámicos
    st.header("Agregar registro")
    escalador = input_escalador(df)
    escalada_con = input_escalada_con(df, escalador)
    st.markdown("---")
    fecha = input_fecha()
    rocodromo = input_rocodromo()
    tipo_via = input_tipo_via(rocodromo)
    dificultad_oficial, opciones_dificultad = input_dificultad_oficial(rocodromo, tipo_via)
    tipo_ascension = input_tipo_ascension()
    intentos = input_intentos(tipo_ascension)
    dificultad_percibida = input_dificultad_percibida(dificultad_oficial, opciones_dificultad)
    valoracion = input_valoracion()
    st.markdown("---")
    comentarios_personales = input_comentarios_personales()
    comentarios_tipo_ascension = input_comentarios_tipo_ascension()
    st.markdown("---")
    nombre_via = input_nombre_via(df, rocodromo)
    st.markdown("---")


    with st.form(key="formulario_usuario"):
        ruta_foto = input_foto(escalador, fecha.strftime("%Y-%m-%d"), CLIENT_ID)
        submit_button = st.form_submit_button("Guardar")

    if submit_button:
        nuevo_registro = {
            "escalador": escalador,
            "escalada_con": escalada_con,
            "fecha": fecha.strftime("%Y-%m-%d"),
            "rocodromo": rocodromo,
            "tipo_via": tipo_via,
            "dificultad_oficial": dificultad_oficial,
            "tipo_ascension": tipo_ascension,
            "intentos": intentos,
            "dificultad_percibida": dificultad_percibida,
            "valoracion": valoracion,
            "comentarios_personales": comentarios_personales,
            "comentarios_tipo_ascension": comentarios_tipo_ascension,
            "nombre_via": nombre_via,
            "ruta_imagen": ruta_foto
        }

        try:
            supabase.table("climbing_data").upsert(nuevo_registro).execute()
            st.success("Registro guardado correctamente")
            st.rerun()
        except Exception as e:
            st.error(f"Error al guardar el registro: {str(e)}")

    st.markdown("---")
    st.subheader("🗑️ Eliminar registro")

    if not df.empty:
        fila_a_borrar = st.number_input("Selecciona el número de fila a borrar", 
                                       min_value=0, 
                                       max_value=len(df) - 1,
                                       value=len(df)-1, 
                                       step=1)

        if st.button("Borrar fila"):
            try:
                id_a_borrar = df.iloc[fila_a_borrar]["supabase_id"]
                supabase.table("climbing_data").delete().eq("supabase_id", id_a_borrar).execute()
                st.success(f"Fila {fila_a_borrar} eliminada correctamente.")
                st.rerun()
            except Exception as e:
                st.error(f"Error al eliminar el registro: {str(e)}")
    else:
        st.info("No hay datos para eliminar.")

# ---------- PESTAÑAS ----------
tab1, tab2, tab3 = st.tabs(["📋 Tabla de datos", "📈 Evolución grado (Boulder)", "📈 Evolución grado (Cuerda)"])

with tab1:
    st.header("📋 Datos recogidos")
    st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("📈 Evolución del grado de escalada a lo largo del tiempo")

    if not df.empty:
        if "Boulder" not in df["tipo_via"].unique():
            st.warning("No hay datos de escalada en boulder.")
        else:
            df_filtrado = evolucion_dificultad_boulder_escalada_tiempo(df)
            kpis_evolucion_dificultad_boulder_escalada_tiempo(df_filtrado)

with tab3:
    st.subheader("📈 Evolución del grado de escalada a lo largo del tiempo")

    if not df.empty:
        if "Cuerda" not in df["tipo_via"].unique():
            st.warning("No hay datos de escalada en cuerda.")
        else:
            df_filtrado = evolucion_dificultad_cuerda_escalada_tiempo(df)
            kpis_evolucion_dificultad_cuerda_escalada_tiempo(df_filtrado)
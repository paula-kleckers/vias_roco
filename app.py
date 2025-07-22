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


# ---------- CONFIGURACIÓN INICIAL ----------
st.set_page_config(page_title="Roco Climber", layout="wide")

#DATA_FILE = "data.csv"

# Tus credenciales de Supabase
url = "https://ubnslrintcfolygbnqsb.supabase.co"
with open("client_id/supabase_key.txt", "r") as f:
    key = f.read().strip()
supabase: Client = create_client(url, key)

with open("client_id/client_id.txt", "r") as f:
    CLIENT_ID = f.read().strip()

# Cargar datos si existen
try:
    response = supabase.table("climbing_data").select("*").execute()
    df = pd.DataFrame(response.data)
except Exception as e:
    st.error("Error al cargar los datos desde Supabase")
    df = pd.DataFrame(columns=[
        "escalador", "escalada_con", "fecha", "rocodromo", "tipo_via", "dificultad_oficial",
        "tipo_ascension", "intentos", "dificultad_percibida", "valoracion",
        "comentarios_personales", "comentarios_tipo_ascension", "nombre_via", "ruta_imagen"
    ])

# if os.path.exists(DATA_FILE):
#     df = pd.read_csv(DATA_FILE)
# else:
#     df = pd.DataFrame(columns=["Escalador", "Nombre vía", "Rocódromo", "Tipo de vía", "Dificultad oficial", "Fecha",
#                                "Tipo de ascensión", "Intentos (en la fecha)", "Dificultad percibida", "Valoración",
#                                "Escalada con...", "Comentarios (personales)", "Comentarios (tipo de ascensión)"])

# ---------- FORMULARIO ----------
with st.sidebar:
    # Botón para reiniciar el formulario
    if st.button("🔄 Resetear formulario"):
        st.session_state.clear()

    st.header("Índice de fila para el registro")
    indice = input_indice(df)
    st.markdown("---")

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
    ruta_foto = input_foto(escalador, fecha.strftime("%Y-%m-%d"), CLIENT_ID)

    # Se genera el formulario para poder utilizar el botón de guardado
    with st.form(key="formulario_usuario"):
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

        if len(df) > 0 and indice < len(df):
            df.loc[indice] = nuevo_registro
        else:
            df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)

        #df.to_csv(DATA_FILE, index=False)
        supabase.table("climbing_data").upsert(nuevo_registro).execute()

        if "registro_seleccionado" in st.session_state:
            del st.session_state["registro_seleccionado"]
        st.success("Registro guardado correctamente")

    st.markdown("---")
    st.subheader("🗑️ Eliminar registro")

    if not df.empty:
        fila_a_borrar = st.number_input("Selecciona el número de fila a borrar", min_value=0, max_value=len(df) - 1,
                                        step=1)

        if st.button("Borrar fila"):
            # df = df.drop(index=fila_a_borrar).reset_index(drop=True)
            # df.to_csv(DATA_FILE, index=False)
            # st.success(f"Fila {fila_a_borrar} eliminada correctamente.")
            id_a_borrar = df.iloc[fila_a_borrar]["supabase_id"]
            supabase.table("climbing_data").delete().eq("supabase_id", id_a_borrar).execute()
            st.success(f"Fila {fila_a_borrar} eliminada correctamente.")

    else:
        st.info("No hay datos para eliminar.")

# ---------- PESTAÑAS ----------
tab1, tab2 = st.tabs(["📋 Tabla de datos", "📊 Gráficos"])

with tab1:
    st.header("📋 Datos recogidos")
    st.dataframe(df, use_container_width=True)

with tab2:
    st.header("📊 Visualización de datos")
    col1, col2 = st.columns(2)

    with col1:
        n_vias_escaladas_por_dificultad_y_escalador(df)
#
#     with col2:
#         st.subheader("Nivel de satisfacción")
#         st.bar_chart(df["Satisfacción"].value_counts().sort_index())
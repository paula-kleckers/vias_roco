import streamlit as st
import pandas as pd
import os
from supabase import create_client, Client

from datetime import datetime, date

# Tus credenciales de Supabase
url = "https://ubnslrintcfolygbnqsb.supabase.co"
with open("client_id/supabase_key.txt", "r") as f:
    key = f.read().strip()
supabase: Client = create_client(url, key)

# def load_data_from_supabase():
#     try:
#         response = supabase.table("climbing_data").select("*").execute()
#         return pd.DataFrame(response.data)
#     except Exception as e:
#         st.error("Error al cargar los datos desde Supabase")
#         return pd.DataFrame(columns=[
#             "escalador", "escalada_con", "fecha", "rocodromo", "tipo_via", "dificultad_oficial",
#             "tipo_ascension", "intentos", "dificultad_percibida", "valoracion",
#             "comentarios_personales", "comentarios_tipo_ascension", "nombre_via", "ruta_imagen"
#         ])

def cargar_valores_indice(df, indice):
    # Si el índice es válido y ha cambiado, actualizamos session_state
    if "indice_actual" not in st.session_state or st.session_state.indice_actual != indice:
        st.session_state.indice_actual = indice
        if 0 <= indice < len(df):
            fila = df.iloc[indice]
            # Escalador
            st.session_state.nombre_escalador = fila.get("escalador", "")
            # Escalada con
            st.session_state.escalada_con_existente = cargar_escalada_con_desde_fila(fila)
            st.session_state.companeros = []  # Los nuevos no están en la base
            # Fecha
            st.session_state.fecha = cargar_fecha_desde_fila(fila)

            #TODO: Cargar los demás campos de la fila

        else:
            # índice no válido → limpiar campos
            st.session_state.nombre_escalador = ""
            st.session_state.escalada_con_existente = []
            st.session_state.fecha = date.today()
            # ... limpiar los demás campos

            # TODO: Limpiar los demás campos de la fila


def cargar_escalada_con_desde_fila(fila):
    """
        Carga en st.session_state.escalada_con_existente el valor de 'escalada_con'
        de la fila pasada, siempre que no esté vacío ni sea [].
    """

    valor_escalada_con = fila.get("escalada_con", "")

    if isinstance(valor_escalada_con, str):
        lista = [x.strip() for x in valor_escalada_con.split(",") if x.strip()]
    elif isinstance(valor_escalada_con, list):
        lista = [x.strip() for x in valor_escalada_con if isinstance(x, str) and x.strip()]
    else:
        lista = []

    return lista

def cargar_fecha_desde_fila(fila):
    valor_fecha = fila.get("fecha", "")
    if valor_fecha:
        if isinstance(valor_fecha, str):
            try:
                return datetime.strptime(valor_fecha, "%Y-%m-%d").date()
            except:
                return date.today()
        elif isinstance(valor_fecha, (datetime, date)):
            return valor_fecha if isinstance(valor_fecha, date) else valor_fecha.date()
    return date.today()
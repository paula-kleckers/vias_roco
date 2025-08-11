import streamlit as st
import pandas as pd
import os
from supabase import create_client, Client

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
            st.session_state.es_nuevo_escalador = False
            st.session_state.nombre_escalador = fila.get("escalador", "")
            st.session_state.escalada_con_existente = fila.get("escalada_con", "").split(", ")
            # ... aquí inicializas todos los campos con valores de esa fila
        else:
            # índice no válido → limpiar campos
            st.session_state.es_nuevo_escalador = False
            st.session_state.nombre_escalador = ""
            st.session_state.escalada_con_existente = []
            # ... limpiar los demás campos
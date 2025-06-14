import streamlit as st

def input_tipo_ascension():
    opciones = ["👀 A vista",
                "⚡ Flash",
                "✅ Completada",
                "❌ Intentada",
                "🪢 Top rope",
                "📚 Proyecto",
                "🗑 Eliminada"]
    return st.selectbox("Tipo de ascensión", opciones)

import streamlit as st

def input_valoracion():
    opciones = ["",
                "🔛 Calentamiento",
                "🥱 Aburrida",
                "☠ Criminal",
                "😫 Muy mala",
                "😕 Mala",
                "😐 Media",
                "😋 Buena",
                "😁 Muy buena",
                "🤪 Locura para bien"]
    return st.selectbox("Valoración de la vía", opciones,
                        help="Selecciona tu valoración de la vía")

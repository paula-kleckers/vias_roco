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

    valor_actual = st.session_state.get("valoracion", "")
    index = opciones.index(valor_actual) if valor_actual in opciones else 0

    return st.selectbox("Valoración de la vía", opciones, index=index,
                        help="Selecciona tu valoración de la vía")

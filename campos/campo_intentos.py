import streamlit as st


def input_intentos(tipo_ascension):

    if tipo_ascension == "👀 A vista" or tipo_ascension == "⚡ Flash":
        # Si es A vista o Flash, no se permite más de un intento
        intentos = st.number_input("Intentos (en la fecha seleccionada)", value=1, disabled=True)

    elif tipo_ascension == "✅ Completada":
        # Si es Completada, se permite cualquier número de intentos mayor que 1
        intentos = st.number_input("Intentos (en la fecha seleccionada)", min_value=2, max_value=100, step=1)

    elif tipo_ascension == '📚 Proyecto' or tipo_ascension == "🗑 Eliminada":
        # Si es Proyecto o Eliminada, no se permite ningún intento en la fecha seleccionada
        intentos = st.number_input("Intentos (en la fecha seleccionada)", value=0, disabled=True)

    else:
        # Si es Intentada o Top Rope, se permite cualquier número de intentos mayor que 1
        intentos = st.number_input("Intentos (en la fecha seleccionada)", min_value=1, max_value=100, step=1)

    return intentos

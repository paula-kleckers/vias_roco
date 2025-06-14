import streamlit as st

def input_nombre_via(df, rocodromo_seleccionado):
    st.header("Nombre de la vía")

    # Contar cuántas vías hay ya para este rocódromo
    vias_existentes = df[df["Rocódromo"] == rocodromo_seleccionado]
    indice = len(vias_existentes) + 1  # siguiente número

    # Campo para comentario extra opcional
    comentario_extra = st.text_input("Comentario adicional para la vía (opcional)", "")

    # Construir nombre
    nombre_via = f"{rocodromo_seleccionado}_{indice}"
    if comentario_extra.strip():
        nombre_via += f"_{comentario_extra.strip().replace(' ', '_')}"

    st.text(f"Nombre generado automáticamente: {nombre_via}")

    return nombre_via

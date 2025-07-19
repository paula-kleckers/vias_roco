import streamlit as st

def input_nombre_via(df, rocodromo_seleccionado):
    st.header("Nombre de la vía")

    # Verificar que la columna 'rocodromo' existe y contiene datos válidos
    if "rocodromo" in df.columns and df["rocodromo"].notna().any():
        vias_existentes = df[df["rocodromo"] == rocodromo_seleccionado]
        indice = len(vias_existentes) + 1
    else:
        indice = 1  # Si no hay datos, comenzamos desde 1

    # Campo para comentario extra opcional
    comentario_extra = st.text_input("Comentario adicional para la vía (opcional)", "")

    # Construir nombre
    nombre_via = f"{rocodromo_seleccionado} {indice}"
    if comentario_extra.strip():
        nombre_via += f" {comentario_extra.strip().replace('_', ' ').replace('-', ' ')}"

    st.text(f"Nombre generado automáticamente: {nombre_via}")

    return nombre_via

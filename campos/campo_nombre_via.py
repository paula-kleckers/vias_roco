import streamlit as st

def input_nombre_via(df, rocodromo_seleccionado):
    st.header("Nombre de la vía")

    # Si no existe el nombre_via en session_state o se ha cambiado el rocódromo
    if ("nombre_via" not in st.session_state or 
        st.session_state.get("ultimo_rocodromo", "") != rocodromo_seleccionado):
        
        # Verificar que la columna 'rocodromo' existe y contiene datos válidos
        if "rocodromo" in df.columns and df["rocodromo"].notna().any():
            vias_existentes = df[df["rocodromo"] == rocodromo_seleccionado]
            indice = len(vias_existentes) + 1
        else:
            indice = 1  # Si no hay datos, comenzamos desde 1

        nombre_via = f"{rocodromo_seleccionado} {indice}"
        st.session_state.nombre_via = nombre_via
        st.session_state.ultimo_rocodromo = rocodromo_seleccionado
    else:
        nombre_via = st.session_state.nombre_via

    st.text(f"Nombre generado automáticamente: {nombre_via}")

    return nombre_via

import streamlit as st
import os
from datetime import datetime
from PIL import Image


def input_foto(nombre_escalador: str, fecha: str):
    st.subheader("Foto de la vía (opcional)")

    imagen = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"], key="foto")

    if imagen:
        # Crear carpeta si no existe
        carpeta = "uploads"
        os.makedirs(carpeta, exist_ok=True)

        # Generar nombre de archivo único
        base_name = f"{nombre_escalador}_{fecha}".replace(" ", "_").replace("/", "-")
        existing = [
            f for f in os.listdir(carpeta)
            if f.startswith(base_name)
        ]
        indice = len(existing) + 1  # siguiente índice
        extension = imagen.name.split(".")[-1]
        filename = f"{base_name}.{extension}"
        ruta_completa = os.path.join(carpeta, filename)

        # Guardar imagen en disco
        with open(ruta_completa, "wb") as f:
            f.write(imagen.getbuffer())

        # Mostrar imagen
        st.image(ruta_completa, caption="Imagen subida", use_container_width=True)

        return ruta_completa  # Ruta que puedes guardar en el DataFrame

    return ""  # Si no se sube imagen, devuelve cadena vacía

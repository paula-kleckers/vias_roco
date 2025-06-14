import streamlit as st
import requests

def subir_a_imgur(imagen_file, client_id):
    headers = {"Authorization": f"Client-ID {client_id}"}
    url = "https://api.imgur.com/3/image"

    imagen_bytes = imagen_file.read()
    data = {
        'image': imagen_bytes,
        'type': 'file'
    }

    response = requests.post(url, headers=headers, files={'image': imagen_bytes})
    if response.status_code == 200:
        link = response.json()['data']['link']
        return link
    else:
        st.error(f"Error subiendo imagen a Imgur: {response.status_code}")
        return None

def input_foto(nombre_escalador: str, fecha: str, client_id: str):
    st.subheader("Foto de la vía (opcional)")

    imagen = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"], key="foto")

    if imagen:
        url_imgur = subir_a_imgur(imagen, client_id)
        if url_imgur:
            st.image(url_imgur, caption="Imagen subida a Imgur", use_container_width=True)
            html_img = f'<img src="{url_imgur}" width="100"/>'
            return html_img
        else:
            return ""
    return ""

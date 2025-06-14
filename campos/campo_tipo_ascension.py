import streamlit as st

def input_tipo_ascension():
    opciones = ["",
                "👀 A vista",
                "⚡ Flash",
                "✅ Completada",
                "❌ Intentada",
                "🪢 Top rope",
                "📚 Proyecto",
                "🗑 Eliminada"]
    return st.selectbox("Tipo de ascensión", opciones,
                        help="Selecciona la dificultad que crees que debería asignarse a la vía.\n"
                             "👀 A vista: Vía completada en el primer intento sin información previa.\n"
                             "⚡ Flash: Vía completada en el primer intento con información previa.\n"
                             "✅ Completada: Vía completada, pero no en el primer intento o parando/cayendo durante "
                             "la subida.\n"
                             "❌ Intentada: Vía intentada pero no completada.\n"
                             "🪢 Top rope: Vía completada en top rope.\n"
                             "📚 Proyecto: Vía que se planea escalar pero no se ha intentado todavía.\n"
                             "🗑 Eliminada: Vía ya no disponible para escalar en el rocódromo.")

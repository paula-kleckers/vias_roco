import streamlit as st
import plotly.express as px
import pandas as pd

def evolucion_dificultad_escalada_tiempo(df):

    if df.empty:
        st.info("No hay datos para mostrar.")
        return

    # Asegurarse que la fecha sea datetime
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df = df.dropna(subset=["fecha", "dificultad_oficial", "tipo_via", "escalador"])

    # Filtros
    escaladores = df["escalador"].dropna().unique()
    tipos_via = df["tipo_via"].dropna().unique()

    col1, col2 = st.columns(2)
    with col1:
        escalador_sel = st.selectbox("Selecciona escalador", sorted(escaladores))
    with col2:
        tipo_via_sel = st.selectbox("Selecciona tipo de vía", sorted(tipos_via))

    # Filtrado
    df_filtrado = df[
        (df["escalador"] == escalador_sel) &
        (df["tipo_via"].str.lower() == tipo_via_sel.lower())
    ]

    if df_filtrado.empty:
        st.warning("No hay datos para esta combinación.")
        return

    # Agrupación: fecha y dificultad oficial
    agrupado = df_filtrado.groupby(["fecha", "dificultad_oficial"]).size().reset_index(name="conteo")
    agrupado = agrupado.sort_values("fecha")

    # Gráfico apilado por dificultad
    fig = px.bar(
        agrupado,
        x="fecha",
        y="conteo",
        color="dificultad_oficial",
        title=f"Vías escaladas por fecha y dificultad – {escalador_sel} ({tipo_via_sel})",
        labels={
            "fecha": "Fecha",
            "conteo": "Número de vías",
            "dificultad_oficial": "Dificultad"
        },
    )

    fig.update_layout(
        barmode="stack",
        xaxis_title="Fecha",
        yaxis_title="Número de vías",
        legend_title="Dificultad oficial"
    )

    st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import plotly.express as px
import pandas as pd

import campos.seleccion_roco_tipo_dif as clas_dif

def evolucion_dificultad_cuerda_escalada_tiempo(df):
    if df.empty:
        st.info("No hay datos para mostrar.")
        return

    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df = df.dropna(subset=["fecha", "dificultad_oficial", "tipo_via", "escalador"])

    # Filtros
    escaladores = df["escalador"].dropna().unique()
    tipos_via = df["tipo_via"].dropna().unique()
    opciones_agrupado = {
        "Día": "D",
        "Mes": "M",
        "Año": "Y"
    }

    col1, col2, col3 = st.columns(3)
    with col1:
        escalador_sel = st.selectbox("Escalador", sorted(escaladores), key="select_escalador_font")
    with col2:
        agrupado_sel = st.selectbox("Agrupar por", list(opciones_agrupado.keys()), key="select_agrupado_font")

    tipo_via_sel = "Cuerda"  # Sólo cuerda para este gráfico

    df_filtrado = df[
        (df["escalador"] == escalador_sel) &
        (df["tipo_via"].str.lower() == tipo_via_sel.lower())
    ].copy()

    if df_filtrado is None or df_filtrado.empty:
        st.warning("No hay datos para esta combinación.")
        return

    # Aplicar conversión condicional
    df_filtrado["grado_fontainebleau"] = df_filtrado["dificultad_oficial"].apply(clas_dif.convertir_si_vscale)

    # Filtrar solo vías completadas
    vias_completadas = ["👀 A vista", "⚡ Flash", "✅ Completada"]
    df_filtrado = df_filtrado[df_filtrado["tipo_ascension"].isin(vias_completadas)]

    # Formatear y agrupar según la selección
    if agrupado_sel == "Día":
        df_filtrado["fecha_agrupada"] = df_filtrado["fecha"]
        df_filtrado["fecha_formateada"] = df_filtrado["fecha"].dt.strftime("%d-%m-%Y")
    elif agrupado_sel == "Mes":
        df_filtrado["fecha_agrupada"] = df_filtrado["fecha"].dt.to_period('M').dt.to_timestamp()
        df_filtrado["fecha_formateada"] = df_filtrado["fecha"].dt.strftime("%m-%Y")
    else:  # Año
        df_filtrado["fecha_agrupada"] = df_filtrado["fecha"].dt.to_period('Y').dt.to_timestamp()
        df_filtrado["fecha_formateada"] = df_filtrado["fecha"].dt.strftime("%Y")
    
    # Agrupar por fecha y dificultad
    agrupado = df_filtrado.groupby(["fecha_agrupada", "fecha_formateada", "grado_fontainebleau"]).size().reset_index(name="conteo")
    
    # Ordenar cronológicamente
    agrupado = agrupado.sort_values("fecha_agrupada")

    fig = px.bar(
        agrupado,
        x="fecha_formateada",
        y="conteo",
        color="grado_fontainebleau",  # Mostramos ambas dificultades
        title=f"Vías escaladas – {escalador_sel} ({tipo_via_sel}) agrupadas por {agrupado_sel}",
        labels={
            "fecha_formateada": "Fecha",
            "conteo": "Número de vías",
            "grado_fontainebleau": "Dificultad oficial"
        }
    )

    fig.update_layout(
        barmode="stack",
        xaxis_title="Fecha",
        yaxis_title="Número de vías",
        legend_title="Dificultad",
        yaxis=dict(rangemode="nonnegative", fixedrange=False),
        xaxis=dict(
            type="category",
            categoryorder="array",
            categoryarray=agrupado["fecha_formateada"].unique(),
            tickangle=45
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    return df_filtrado

def kpis_evolucion_dificultad_cuerda_escalada_tiempo(df_filtrado):
    if df_filtrado is None or df_filtrado.empty:
        st.warning("No hay datos para esta combinación.")
        return

    col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
    col_kpi1_below, col_kpi2_below, col_kpi3_below = st.columns(3)

    # Total vías escaladas
    total_vias = len(df_filtrado)

    # Dificultad máxima en Fontainebleau
    dificultad_max_font = "-"
    dificultad_frec = "-"
    frecuencia_frec = 0
    veces_max = 0

    if "grado_fontainebleau" in df_filtrado.columns:
        orden_font = [
            "4", "4+",
            "5", "5+",
            "6a", "6a+", "6b", "6b+", "6c", "6c+",
            "7a", "7a+", "7b", "7b+", "7c", "7c+",
            "8a", "8a+", "8b", "8b+", "8c", "8c+",
            "9a", "9a+", "9b", "9b+", "9c"
        ]

        dificultades_font = df_filtrado["grado_fontainebleau"].dropna().unique().tolist()
        dificultades_font_validas = [x for x in dificultades_font if x in orden_font]

        if dificultades_font_validas:
            dificultad_max_font = max(dificultades_font_validas, key=lambda x: orden_font.index(x))

        # Dificultad más escalada (moda) y frecuencia
        if not df_filtrado["grado_fontainebleau"].dropna().empty:
            dificultad_frec = df_filtrado["grado_fontainebleau"].mode()[0]
            frecuencia_frec = df_filtrado["grado_fontainebleau"].value_counts()[dificultad_frec]

        # Veces que se ha escalado la dificultad máxima
        if dificultad_max_font != "-":
            veces_max = df_filtrado[df_filtrado["grado_fontainebleau"] == dificultad_max_font].shape[0]

    # Mostrar KPIs en dos filas
    col_kpi1.metric("🔢 Total vías escaladas", total_vias)
    col_kpi2.metric("🔥 Dificultad más repetida", dificultad_frec)
    col_kpi3.metric(f"🔥 Total vías dificultad más repetida ({dificultad_frec})", frecuencia_frec)

    col_kpi2_below.metric("⛰️ Dificultad máxima", dificultad_max_font)
    col_kpi3_below.metric(f"⛰️ Total vías dificultad máxima ({dificultad_max_font})", veces_max)


import streamlit as st
import plotly.express as px
import pandas as pd

def evolucion_dificultad_escalada_tiempo(df):

    if df.empty:
        st.info("No hay datos para mostrar.")
        return

    # Asegurar formato correcto
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
        escalador_sel = st.selectbox("Escalador", sorted(escaladores), key="select_escalador_apilado")
    with col2:
        tipo_via_sel = st.selectbox("Tipo de vía", sorted(tipos_via), key="select_tipo_via_apilado")
    with col3:
        agrupado_sel = st.selectbox("Agrupar por", list(opciones_agrupado.keys()), key="select_agrupado_apilado")

    # Filtrado de datos
    df_filtrado = df[
        (df["escalador"] == escalador_sel) &
        (df["tipo_via"].str.lower() == tipo_via_sel.lower())
    ]

    if df_filtrado.empty:
        st.warning("No hay datos para esta combinación.")
        return

    # Agrupación por período
    freq = opciones_agrupado[agrupado_sel]
    df_filtrado["fecha_agrupada"] = df_filtrado["fecha"].dt.to_period(freq).dt.to_timestamp()

    # Formateo personalizado de la fecha para mostrarla como texto limpio
    if agrupado_sel == "Día":
        df_filtrado["fecha_formateada"] = df_filtrado["fecha_agrupada"].dt.strftime("%d-%m-%Y")
    elif agrupado_sel == "Mes":
        df_filtrado["fecha_formateada"] = df_filtrado["fecha_agrupada"].dt.strftime("%m-%Y")
    elif agrupado_sel == "Año":
        df_filtrado["fecha_formateada"] = df_filtrado["fecha_agrupada"].dt.strftime("%Y")

    # Agrupar por fecha formateada y dificultad
    agrupado = df_filtrado.groupby(["fecha_agrupada", "fecha_formateada", "dificultad_oficial"]).size().reset_index(name="conteo")

    # Orden cronológico
    agrupado = agrupado.sort_values("fecha_agrupada")

    # Gráfico
    fig = px.bar(
        agrupado,
        x="fecha_formateada",
        y="conteo",
        color="dificultad_oficial",
        title=f"Vías escaladas – {escalador_sel} ({tipo_via_sel}) agrupadas por {agrupado_sel}",
        labels={
            "fecha_formateada": "Fecha",
            "conteo": "Número de vías",
            "dificultad_oficial": "Dificultad"
        }
    )

    fig.update_layout(
        barmode="stack",
        xaxis_title="Fecha",
        yaxis_title="Número de vías",
        legend_title="Dificultad",
        yaxis=dict(
            rangemode="nonnegative",
            fixedrange=False
        )
    )

    fig.update_xaxes(tickmode="linear", tickformat=".0f")  # Para X solo si interpreta como número

    st.plotly_chart(fig, use_container_width=True)

    return df_filtrado

def kpis_evolucion_dificultad_escalada_tiempo(df_filtrado):

    # --- KPIs debajo del gráfico ---
    df_kpi = df_filtrado.copy()

    # Total de vías
    total_vias = len(df_kpi)

    # Dificultad más escalada (modo)
    if not df_kpi.empty:
        dificultad_mas_escalada = df_kpi["dificultad_oficial"].mode()[0]
        total_mas_escalada = (df_kpi["dificultad_oficial"] == dificultad_mas_escalada).sum()

        # Dificultad máxima escalada (alfabéticamente o numéricamente)
        dificultad_maxima = df_kpi["dificultad_oficial"].max()
        total_maxima = (df_kpi["dificultad_oficial"] == dificultad_maxima).sum()
    else:
        dificultad_mas_escalada = "-"
        total_mas_escalada = 0
        dificultad_maxima = "-"
        total_maxima = 0

    # Mostrar KPIs debajo del gráfico
    st.markdown("### 📌 Resumen de actividad")

    col1, col2, col3 = st.columns(3)
    col1.metric("🔢 Total vías escaladas", total_vias)
    col2.metric(f"🔥 Dificultad más repetida", dificultad_mas_escalada)
    col3.metric(f"⛰️ Dificultad máxima", dificultad_maxima)

    col1_below, col2_below, col3_below = st.columns(3)
    # col1_below sirve para alinear el resto de KPIs
    col2_below.metric(f"🔥 Total vías dificultad más repetida ({dificultad_mas_escalada})", total_mas_escalada)
    col3_below.metric(f"⛰️ Total vías dificultad máxima ({dificultad_maxima})", total_maxima)

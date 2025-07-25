import streamlit as st
import plotly.express as px
import pandas as pd

import campos.seleccion_roco_tipo_dif as clas_dif

# Convertir dificultad oficial a dificultad estandar
def obtener_color_estandar(row):
    rocodromo = row.get("rocodromo", "").strip()
    dificultad_oficial = row.get("dificultad_oficial", "").strip()

    if rocodromo in ["Climbat", "One Move"]:
        return clas_dif.convertir_color_rocodromo_a_estandar(rocodromo, dificultad_oficial)
    elif rocodromo == "Adamanta Gonzalitos":
        return clas_dif.convertir_vscale_a_color_estandar(dificultad_oficial)
    else:
        return clas_dif.convertir_fontainebleau_a_color_estandar(dificultad_oficial)


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
    ].copy()

    if df_filtrado.empty:
        st.warning("No hay datos para esta combinación.")
        return

    df_filtrado["dificultad_color_estandar"] = df_filtrado.apply(obtener_color_estandar, axis=1)

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

    # Agrupar por fecha y dificultad estándar
    agrupado = df_filtrado.groupby(["fecha_agrupada", "fecha_formateada", "dificultad_color_estandar"]).size().reset_index(name="conteo")

    # Orden cronológico
    agrupado = agrupado.sort_values("fecha_agrupada")

    # Gráfico
    fig = px.bar(
        agrupado,
        x="fecha_formateada",
        y="conteo",
        color="dificultad_color_estandar",
        title=f"Vías escaladas – {escalador_sel} ({tipo_via_sel}) agrupadas por {agrupado_sel}",
        labels={
            "fecha_formateada": "Fecha",
            "conteo": "Número de vías",
            "dificultad_estandar": "Dificultad (estándar)"
        },
        color_discrete_map={
            clas_dif.dificultad_estandar_boulder[0]: "#d6d6d6",
            clas_dif.dificultad_estandar_boulder[1]: "#ffd700",
            clas_dif.dificultad_estandar_boulder[2]: "#e67e22",
            clas_dif.dificultad_estandar_boulder[3]: "#58d68d",
            clas_dif.dificultad_estandar_boulder[4]: "#5dade2",
            clas_dif.dificultad_estandar_boulder[5]: "#ec7063",
            clas_dif.dificultad_estandar_boulder[6]: "#2c3e50"
        },
        category_orders={
            "dificultad_color_estandar": clas_dif.dificultad_estandar_boulder
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

    fig.update_xaxes(tickmode="linear", tickformat=".0f")

    st.plotly_chart(fig, use_container_width=True)

    return df_filtrado


# --- KPIs ---
def kpis_evolucion_dificultad_escalada_tiempo(df_filtrado):
    ranking_dificultad = {
        clas_dif.dificultad_estandar_boulder[0]: 0,
        clas_dif.dificultad_estandar_boulder[1]: 1,
        clas_dif.dificultad_estandar_boulder[2]: 2,
        clas_dif.dificultad_estandar_boulder[3]: 3,
        clas_dif.dificultad_estandar_boulder[4]: 4,
        clas_dif.dificultad_estandar_boulder[5]: 5,
        clas_dif.dificultad_estandar_boulder[6]: 6
    }

    df_kpi = df_filtrado.copy()
    total_vias = len(df_kpi)

    dificultades_validas = [d for d in df_kpi["dificultad_color_estandar"].dropna().unique() if d in ranking_dificultad]

    if dificultades_validas:
        dificultad_maxima = max(dificultades_validas, key=lambda x: ranking_dificultad[x])
    else:
        dificultad_maxima = "-"

    modo = df_kpi["dificultad_color_estandar"].mode()
    if not modo.empty and modo[0] in ranking_dificultad:
        dificultad_mas_escalada = modo[0]
        total_mas_escalada = (df_kpi["dificultad_color_estandar"] == dificultad_mas_escalada).sum()
    else:
        dificultad_mas_escalada = "-"
        total_mas_escalada = 0

    total_maxima = (df_kpi["dificultad_color_estandar"] == dificultad_maxima).sum() if dificultad_maxima != "-" else 0

    st.markdown("### 📌 Resumen de actividad")

    col1, col2, col3 = st.columns(3)
    col1.metric("🔢 Total vías escaladas", total_vias)
    col2.metric(f"🔥 Dificultad más repetida", dificultad_mas_escalada)
    col3.metric(f"⛰️ Dificultad máxima", dificultad_maxima)

    col1_below, col2_below, col3_below = st.columns(3)
    col2_below.metric(f"🔥 Total vías dificultad más repetida ({dificultad_mas_escalada})", total_mas_escalada)
    col3_below.metric(f"⛰️ Total vías dificultad máxima ({dificultad_maxima})", total_maxima)

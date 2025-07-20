import plotly.express as px
import streamlit as st

def dificultad_por_escalador(df):
    st.subheader("📈 Vías por dificultad (Plotly)")

    if df.empty:
        st.info("No hay datos para mostrar.")
        return

    escalador_sel = st.selectbox("Escalador", df["escalador"].dropna().unique())
    rocodromo_sel = st.selectbox("Rocódromo", df["rocodromo"].dropna().unique())
    tipo_via_sel = st.selectbox("Tipo de vía", df["tipo_via"].dropna().unique())

    df_filtrado = df[
        (df["escalador"] == escalador_sel) &
        (df["rocodromo"] == rocodromo_sel) &
        (df["tipo_via"] == tipo_via_sel)
    ]

    if df_filtrado.empty:
        st.warning("No hay datos para esta combinación.")
        return

    conteo = df_filtrado["dificultad_oficial"].value_counts().reset_index()
    conteo.columns = ["dificultad_oficial", "n"]

    fig = px.bar(
        conteo,
        x="dificultad_oficial",
        y="n",
        title=f"{escalador_sel} – {rocodromo_sel} – {tipo_via_sel}",
        labels={"n": "Número de vías", "dificultad_oficial": "Dificultad oficial"},
        color="dificultad_oficial",
        text="n"
    )
    fig.update_layout(xaxis={'categoryorder': 'category ascending'})
    st.plotly_chart(fig, use_container_width=True)

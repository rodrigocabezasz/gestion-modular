# utils/visualizacion.py
"""
Funciones para visualización personalizada en Streamlit (gráficos, tablas, etc).
"""
import streamlit as st
import plotly.express as px

def mostrar_grafico_barra(datos, x, y, titulo):
    """Muestra un gráfico de barras usando Plotly."""
    fig = px.bar(datos, x=x, y=y, title=titulo)
    st.plotly_chart(fig)

def mostrar_tabla(datos):
    """Muestra una tabla en Streamlit."""
    st.dataframe(datos)

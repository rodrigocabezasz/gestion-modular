# utils/estilos.py
"""
Este módulo contiene funciones para aplicar estilos personalizados usando Bootstrap, Google Fonts y Font Awesome en Streamlit.
"""
import streamlit as st

def cargar_bootstrap():
    """Carga los estilos de Bootstrap en la app."""
    st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">', unsafe_allow_html=True)

def cargar_google_fonts():
    """Carga Google Fonts en la app."""
    st.markdown('<link href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap" rel="stylesheet">', unsafe_allow_html=True)

def cargar_font_awesome():
    """Carga los iconos de Font Awesome en la app."""
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)

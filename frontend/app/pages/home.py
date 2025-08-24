# home.py
"""
Página principal de bienvenida para la aplicación multipágina.
"""
import streamlit as st
from utils.estilos import cargar_bootstrap, cargar_google_fonts, cargar_font_awesome

# Cargar estilos personalizados
cargar_bootstrap()
cargar_google_fonts()
cargar_font_awesome()

st.title("Bienvenido al Framework de Gestión")
st.write("Esta es la página principal de la aplicación. Utiliza el menú lateral para navegar entre las diferentes secciones.")

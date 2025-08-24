# login.py
"""
Página de login que interactúa con el backend para autenticación.
"""
import streamlit as st
import requests
from utils.estilos import cargar_bootstrap

cargar_bootstrap()

st.header("Iniciar sesión")
email = st.text_input("Correo electrónico")
password = st.text_input("Contraseña", type="password")

if st.button("Login"):
    # Realiza la petición al backend para obtener el token
    response = requests.post(
        "http://localhost:8000/login",
        json={"email": email, "password": password}
    )
    if response.status_code == 200:
        st.success("Login exitoso")
        st.session_state["token"] = response.json()["access_token"]
    else:
        st.error("Credenciales inválidas")

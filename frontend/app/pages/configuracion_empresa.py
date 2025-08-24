# configuracion_empresa.py
"""
Página para configurar los datos generales de la empresa.
"""
import streamlit as st
from utils.estilos import cargar_bootstrap

cargar_bootstrap()

st.header("Configuración de la Empresa")

# Formulario para datos generales
with st.form("form_empresa"):
    nombre = st.text_input("Nombre de la empresa")
    descripcion = st.text_area("Descripción de la empresa")
    logo = st.file_uploader("Subir logo de la empresa", type=["png", "jpg", "jpeg"])
    direccion = st.text_input("Dirección")
    telefono = st.text_input("Teléfono")
    email = st.text_input("Correo de contacto")
    sitio_web = st.text_input("Sitio web")
    submit = st.form_submit_button("Guardar configuración")

import requests

if submit:
    # Enviar datos al backend
    datos = {
        "nombre": nombre,
        "descripcion": descripcion,
        "logo": logo.name if logo else None,
        "direccion": direccion,
        "telefono": telefono,
        "email": email,
        "sitio_web": sitio_web
    }
    response = requests.post("http://localhost:8000/empresa/config", json=datos)
    if response.status_code == 200:
        st.success("Configuración guardada correctamente.")
    else:
        st.error("Error al guardar la configuración.")
    # Subir logo si existe
    if logo:
        files = {"file": (logo.name, logo, logo.type)}
        resp_logo = requests.post("http://localhost:8000/empresa/logo", files=files)
        if resp_logo.status_code == 200:
            st.image(logo, caption="Logo de la empresa", use_column_width=True)
        else:
            st.error("Error al subir el logo.")

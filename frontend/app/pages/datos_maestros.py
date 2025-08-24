# datos_maestros.py
"""
Página de gestión de datos maestros, accesible solo para administradores.
"""
import streamlit as st
from utils.estilos import cargar_bootstrap

cargar_bootstrap()

st.header("Gestión de Datos Maestros")

with st.form("form_dato_maestro"):
    nombre = st.text_input("Nombre del dato maestro")
    descripcion = st.text_area("Descripción")
    submit = st.form_submit_button("Agregar dato maestro")

if submit:
    st.success("Dato maestro agregado correctamente.")
    # Aquí se puede agregar la lógica para guardar el dato maestro en el backend

st.subheader("Listado de datos maestros")
datos = [
    {"Nombre": "Sucursal", "Descripción": "Puntos de venta físicos"},
    {"Nombre": "Producto", "Descripción": "Artículos comercializados"}
]
st.table(datos)
import requests

# Formulario para agregar un dato maestro
with st.form("form_dato_maestro"):
    nombre = st.text_input("Nombre del dato maestro")
    descripcion = st.text_area("Descripción")
    submit = st.form_submit_button("Agregar dato maestro")

if submit:
    # Enviar dato maestro al backend
    datos = {"nombre": nombre, "descripcion": descripcion}
    response = requests.post("http://localhost:8000/datos_maestros", json=datos)
    if response.status_code == 200:
        st.success("Dato maestro agregado correctamente.")
    else:
        st.error("Error al agregar el dato maestro.")

# Listar datos maestros desde el backend
st.subheader("Listado de datos maestros")
resp_lista = requests.get("http://localhost:8000/datos_maestros")
if resp_lista.status_code == 200:
    datos = resp_lista.json()
    st.table(datos)
else:
    st.error("No se pudo obtener el listado de datos maestros.")

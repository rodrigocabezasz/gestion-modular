# perfil.py
"""
Página de perfil de usuario, accesible para todos los usuarios.
"""
import streamlit as st
from utils.estilos import cargar_bootstrap

cargar_bootstrap()

st.header("Mi Perfil")

# Mostrar información básica del usuario
user_name = st.session_state.get("user_name", "Usuario")
user_email = st.session_state.get("user_email", "correo@empresa.com")
user_role = st.session_state.get("user_role", "Usuario")

st.write(f"**Nombre:** {user_name}")
st.write(f"**Correo:** {user_email}")
st.write(f"**Rol:** {user_role}")

# Formulario para actualizar datos personales
with st.form("form_perfil"):
    nuevo_nombre = st.text_input("Actualizar nombre", value=user_name)
    nuevo_email = st.text_input("Actualizar correo", value=user_email)
    submit = st.form_submit_button("Guardar cambios")

if submit:
    st.success("Datos actualizados correctamente.")
    # Aquí se puede agregar la lógica para actualizar los datos en el backend

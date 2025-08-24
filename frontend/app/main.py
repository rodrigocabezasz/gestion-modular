
import streamlit as st
import requests

import streamlit as st
from menu import mostrar_menu

# Configuración de la página principal
st.set_page_config(page_title="Framework Gestión", layout="wide")
st.sidebar.title("Menú Principal")

# Mostrar menú lateral y navegar entre páginas
opcion = mostrar_menu()

if opcion == "Inicio":
	from pages.home import *
elif opcion == "Usuarios":
	st.subheader("Gestión de Usuarios")
	# Aquí se pueden agregar formularios y tablas para CRUD de usuarios
elif opcion == "Roles":
	st.subheader("Gestión de Roles")
	# Aquí se pueden agregar formularios y tablas para CRUD de roles
elif opcion == "Dashboard":
	st.subheader("Dashboard de Datos")
	# Aquí se pueden mostrar gráficos y KPIs
elif opcion == "Configuración Empresa":
	from pages.configuracion_empresa import *

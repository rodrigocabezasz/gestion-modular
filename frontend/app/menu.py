

# menu.py
"""
Menú lateral genérico y adaptable para cualquier empresa, mostrando logo, nombre de usuario y navegación por rol.
"""
import streamlit as st
from pathlib import Path

# Roles de ejemplo para la plantilla
ADMIN_ROLE = "Administrador"
USER_ROLE = "Usuario"

def generar_menu():
    """
    Genera un menú lateral profesional y adaptable, mostrando logo, nombre de usuario y páginas según el rol logueado.
    Este menú es una plantilla y puede ser personalizado para cualquier empresa.
    """
    if not st.session_state.get("logged_in"):
        return

    # Estilos personalizados para el menú y perfil
    st.markdown("""
        <style>
            [data-testid="stSidebarNav"] { display: none; }
            .profile-section {
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 0.5rem 0;
            }
            .user-name {
                font-size: 1.1rem;
                font-weight: 600;
                color: #31333F;
                margin-top: 0.1rem;
                margin-bottom: 0.1rem;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        # Sección de perfil con logo y nombre de usuario
        st.markdown('<div class="profile-section">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            logo_path = Path(__file__).parent / "assets" / "logo.png"
            if logo_path.exists():
                st.image(str(logo_path))
        user_name = st.session_state.get("user_name", "Usuario")
        st.markdown(f"<div class='user-name'>{user_name}</div>", unsafe_allow_html=True)
        st.subheader("Menú de Navegación")
        st.markdown("---")

        # Navegación principal según rol
        user_role = st.session_state.get("user_role", USER_ROLE)
        st.page_link("pages/home.py", label="Inicio", icon="🏠")

        # Ejemplo: página accesible solo para administradores
        if user_role == ADMIN_ROLE:
            st.page_link("pages/configuracion_empresa.py", label="Configuración de la Empresa", icon="⚙️")
            st.page_link("pages/datos_maestros.py", label="Datos Maestros", icon="📋")

        # Ejemplo: página accesible para todos los usuarios
        st.page_link("pages/perfil.py", label="Mi Perfil", icon="�")

        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Cerrar Sesión", use_container_width=True, type="secondary"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.switch_page("app.py")

        st.markdown("---")

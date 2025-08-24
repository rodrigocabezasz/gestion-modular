# Framework Modular para Dashboards de Control de Gestión

## Descripción
Plantilla base para crear sistemas de dashboards empresariales con autenticación, gestión de datos maestros, ETL y dashboards personalizables.

## Estructura del Proyecto
- **backend/**: API REST con FastAPI.
- **frontend/**: Interfaz de usuario con Streamlit.
- **db/**: Archivos de base de datos y Docker Compose.
- **docs/**: Documentación.

## Instalación y Configuración Inicial
1. Clona el repositorio.
2. Levanta la base de datos MySQL con Docker:
   ```powershell
   cd db
   docker-compose up -d
   ```
3. Instala dependencias del backend:
   ```powershell
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
4. Instala dependencias del frontend:
   ```powershell
   cd frontend
   pip install -r requirements.txt
   streamlit run app/main.py
   ```

## Personalización
- Para añadir nuevos datos maestros, crea modelos y endpoints en `backend/app/models` y `backend/app/api`.
- Para crear un nuevo dashboard, añade una página en `frontend/app/pages` y usa componentes de Plotly y Pandas.

## Ejemplo de Uso
- Carga datos maestros desde el frontend.
- Sube archivos para ETL.
- Visualiza dashboards en Streamlit.

## Variables de Entorno
Copia `.env.example` y configura tus credenciales de base de datos y JWT.

---

Para más detalles, consulta la documentación de cada módulo.

## Detalles de Configuración

Para que el sistema funcione correctamente, debes configurar las siguientes variables de entorno en un archivo `.env` (puedes copiar y renombrar `.env.example`):

- `DATABASE_URL`: Cadena de conexión a la base de datos MySQL (ejemplo: `mysql+pymysql://usuario:contraseña@localhost:3306/gestion_modular`).
- `SECRET_KEY`: Clave secreta para la generación de tokens JWT.
- `ALGORITHM`: Algoritmo de cifrado para JWT (por defecto: `HS256`).
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Tiempo de expiración del token de acceso (en minutos).

Recomendaciones:
- No compartas tu archivo `.env` en repositorios públicos.
- Cambia la clave secreta y credenciales antes de desplegar en producción.
- Revisa y ajusta los puertos y rutas en los archivos de Docker y configuración según tu entorno.
## Descripción de Carpetas

- **backend/**: API RESTful, lógica de negocio y modelos de datos (FastAPI).
- **frontend/**: Interfaz de usuario, dashboards y componentes visuales (Streamlit).
- **db/**: Archivos de inicialización y configuración de la base de datos (MySQL, Docker).
- **docs/**: Documentación técnica y ejemplos de uso.
- **.env.example**: Archivo de ejemplo para variables de entorno y configuración.

# Gestion Modular

Framework modular para la gestión empresarial, desarrollado con FastAPI (backend) y Streamlit (frontend). Permite administrar usuarios, roles, datos maestros, configuración de empresa y dashboards personalizables.

## Características principales
- Backend con FastAPI: API RESTful, autenticación JWT, modelos SQLAlchemy, endpoints CRUD.
- Frontend con Streamlit: multipágina, menú dinámico por roles, formularios, carga de archivos y dashboards interactivos.
- Base de datos MySQL gestionada con Docker.
- Estructura adaptable para cualquier empresa o sector.


## Estructura de Carpetas

```text
gestion-modular/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── api/
│   │   ├── core/
│   │   └── utils/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── app/
│   │   ├── main.py
│   │   ├── menu.py
│   │   ├── pages/
│   │   └── utils/
│   ├── requirements.txt
│   └── Dockerfile
│
├── db/
│   ├── init.sql
│   └── docker-compose.yml
│
├── docs/
│   └── README.md
│
└── .env.example
```

## Instalación y Configuración
1. Clona el repositorio:
   ```powershell
   git clone https://github.com/rodrigocabezasz/gestion-modular.git
   ```
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

## Personalización y Extensión
- Agrega nuevos modelos y endpoints en `backend/app/models` y `backend/app/api`.
- Crea dashboards y páginas personalizadas en `frontend/app/pages`.
- Usa los archivos `utils/` para estilos, visualización y funciones comunes.


## Ejemplo de Uso

### Ejemplo de endpoints (backend)

**Registro de usuario:**
```http
POST /register
{
   "username": "usuario1",
   "email": "usuario1@empresa.com",
   "password": "123456",
   "role_id": 1
}
```

**Login:**
```http
POST /login
{
   "email": "usuario1@empresa.com",
   "password": "123456"
}
```

**Agregar dato maestro:**
```http
POST /datos_maestros
{
   "nombre": "Sucursal",
   "descripcion": "Puntos de venta físicos"
}
```

**Configurar empresa:**
```http
POST /empresa/config
{
   "nombre": "Mi Empresa",
   "descripcion": "Empresa dedicada a servicios de gestión",
   "direccion": "Av. Principal 123",
   "telefono": "+56 9 1234 5678",
   "email": "contacto@miempresa.com",
   "sitio_web": "https://miempresa.com"
}
```

### Ejemplo de uso en frontend (Streamlit)

- Configura los datos generales de la empresa y sube el logo desde la página "Configuración de Empresa".
- Administra datos maestros desde la página "Datos Maestros".
- Visualiza dashboards y reportes interactivos en las páginas personalizadas.

## Variables de Entorno
Copia `.env.example` y configura tus credenciales de base de datos y JWT.

---

Palabras clave: FastAPI, Streamlit, gestión, dashboard, empresa, modular, Python, ETL, autenticación, SQLAlchemy, Docker.

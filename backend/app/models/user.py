from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

# Declaración de la base para los modelos
Base = declarative_base()

# Modelo de usuario para la base de datos
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)  # Identificador único del usuario
    username = Column(String(50), unique=True, index=True, nullable=False)  # Nombre de usuario
    email = Column(String(100), unique=True, index=True, nullable=False)  # Correo electrónico
    hashed_password = Column(String(255), nullable=False)  # Contraseña encriptada
    is_active = Column(Boolean, default=True)  # Estado de activación del usuario
    role_id = Column(Integer, nullable=True)  # Relación con el rol del usuario

    def __init__(self, username, email, hashed_password, is_active=True, role_id=None):
        """
        Inicializa un nuevo usuario.
        :param username: Nombre de usuario
        :param email: Correo electrónico
        :param hashed_password: Contraseña encriptada
        :param is_active: Estado de activación
        :param role_id: ID del rol asociado
        """
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active
        self.role_id = role_id

# Modelo de rol para la base de datos
class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)  # Identificador único del rol
    name = Column(String(50), unique=True, nullable=False)  # Nombre del rol
    description = Column(String(255), nullable=True)  # Descripción del rol

    def __init__(self, name, description=None):
        """
        Inicializa un nuevo rol.
        :param name: Nombre del rol
        :param description: Descripción del rol
        """
        self.name = name
        self.description = description

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.user import User, Role
from ..schemas.user import UserCreate, UserRead, RoleCreate, RoleRead
from ..core.security import get_password_hash, verify_password, create_access_token
from ..core.database import get_db

# Inicialización del router para los endpoints de usuario y rol
router = APIRouter()

# Endpoint para registrar un nuevo usuario
@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica si el correo ya está registrado
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    # Encripta la contraseña antes de guardar
    hashed_password = get_password_hash(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_active=True,
        role_id=user.role_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Endpoint para login de usuario
@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    # Busca el usuario por correo
    db_user = db.query(User).filter(User.email == user.email).first()
    # Verifica credenciales
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    access_token = create_access_token({"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint para obtener todos los usuarios
@router.get("/users", response_model=list[UserRead])
def get_users(db: Session = Depends(get_db)):
    # Retorna la lista de todos los usuarios
    return db.query(User).all()

# Endpoint para obtener un usuario por ID
@router.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    # Busca el usuario por su ID
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    # Busca el usuario por su ID
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # Actualiza los campos del usuario usando setattr para evitar problemas con SQLAlchemy
    db_user.username = user.username
    db_user.email = str(user.email)
    db_user.hashed_password = get_password_hash(user.password)
    db_user.is_active = bool(user.is_active)
    db_user.role_id = int(user.role_id) if user.role_id is not None else None
    db.commit()
    db.refresh(db_user)
    return db_user

# Endpoint para eliminar un usuario
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    # Elimina el usuario por su ID
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(db_user)
    db.commit()
    return {"detail": "Usuario eliminado"}

# Endpoint para obtener todos los roles
@router.get("/roles", response_model=list[RoleRead])
def get_roles(db: Session = Depends(get_db)):
    # Retorna la lista de todos los roles
    return db.query(Role).all()

# Endpoint para crear un nuevo rol
@router.post("/roles", response_model=RoleRead)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    # Crea un nuevo rol en la base de datos
    new_role = Role(name=role.name, description=role.description)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

# Endpoint para eliminar un rol
@router.delete("/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    # Elimina el rol por su ID
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    db.delete(db_role)
    db.commit()
    return {"detail": "Rol eliminado"}

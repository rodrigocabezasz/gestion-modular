# backend/app/api/empresa.py
"""
API para la gestión de la configuración de la empresa y datos maestros.
"""
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from ..core.database import get_db
from ..models.empresa import Empresa, DatoMaestro
from ..schemas.empresa import EmpresaConfig, EmpresaConfigRead, DatoMaestroCreate, DatoMaestroRead

router = APIRouter()

# Endpoint para guardar configuración de empresa
@router.post("/empresa/config", response_model=EmpresaConfigRead)
def guardar_config_empresa(config: EmpresaConfig, db: Session = Depends(get_db)):
    empresa = db.query(Empresa).first()
    if not empresa:
        empresa = Empresa(**config.dict())
        db.add(empresa)
    else:
        for key, value in config.dict().items():
            setattr(empresa, key, value)
    db.commit()
    db.refresh(empresa)
    return empresa

# Endpoint para subir logo
@router.post("/empresa/logo")
def subir_logo(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Aquí se guardaría el archivo en el sistema y se actualizaría la ruta en la base de datos
    return {"filename": file.filename}

# Endpoint para agregar dato maestro
@router.post("/datos_maestros", response_model=DatoMaestroRead)
def agregar_dato_maestro(dato: DatoMaestroCreate, db: Session = Depends(get_db)):
    nuevo_dato = DatoMaestro(**dato.dict())
    db.add(nuevo_dato)
    db.commit()
    db.refresh(nuevo_dato)
    return nuevo_dato

# Endpoint para listar datos maestros
@router.get("/datos_maestros", response_model=list[DatoMaestroRead])
def listar_datos_maestros(db: Session = Depends(get_db)):
    return db.query(DatoMaestro).all()

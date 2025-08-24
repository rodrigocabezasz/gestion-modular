# schemas/empresa.py
"""
Esquemas Pydantic para la configuración de la empresa y datos maestros.
"""
from pydantic import BaseModel
from typing import Optional

class EmpresaConfig(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    logo: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    sitio_web: Optional[str] = None

class EmpresaConfigRead(EmpresaConfig):
    id: int
    class Config:
        orm_mode = True

class DatoMaestroCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class DatoMaestroRead(DatoMaestroCreate):
    id: int
    class Config:
        orm_mode = True

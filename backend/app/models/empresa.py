# models/empresa.py
"""
Modelos para la configuración de la empresa y datos maestros.
"""
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresa"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    logo = Column(String(255))
    direccion = Column(String(255))
    telefono = Column(String(50))
    email = Column(String(100))
    sitio_web = Column(String(100))

class DatoMaestro(Base):
    __tablename__ = "datos_maestros"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)

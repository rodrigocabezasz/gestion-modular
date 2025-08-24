# utils/fechas.py
"""
Funciones para trabajar con fechas, meses y días en español.
"""
MES_NOMBRES = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

DIA_NOMBRES = [
    "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"
]

def nombre_mes(numero):
    """Devuelve el nombre del mes en español dado su número (1-12)."""
    return MES_NOMBRES[numero - 1]

def nombre_dia(numero):
    """Devuelve el nombre del día en español dado su número (1-7, lunes=1)."""
    return DIA_NOMBRES[numero - 1]

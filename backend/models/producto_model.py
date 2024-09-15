from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Producto(Base):
    __tablename__ = 'producto'
    
    id_producto = Column(Integer, primary_key=True, index=True)
    imagen = Column(String(255))
    nombre_producto = Column(String(100), nullable=False)
    precio = Column(Integer, nullable=False)
    id_seccion = Column(Integer, ForeignKey('seccion.id_seccion'))

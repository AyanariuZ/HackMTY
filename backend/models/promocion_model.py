from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Promocion(Base):
    __tablename__ = 'promocion'
    
    id_promocion = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id_cliente'))
    titulo = Column(String(255), nullable=False)
    descripcion_promocion = Column(String(255), nullable=False)
    aceptado = Column(Integer, nullable=False)  # 1 para aceptado, 0 para rechazado

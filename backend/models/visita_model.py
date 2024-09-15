from sqlalchemy import Column, Integer, Date, ForeignKey
from .database import Base

class Visita(Base):
    __tablename__ = 'visita'
    
    id_visita = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id_cliente'))
    fecha = Column(Date, nullable=False)

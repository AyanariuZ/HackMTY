from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Cliente(Base):
    __tablename__ = 'cliente'
    
    id_cliente = Column(Integer, primary_key=True, index=True)
    edad = Column(Integer, nullable=False)
    sexo = Column(Integer, nullable=False)  # 0 para mujer, 1 para hombre
    id_cluster = Column(Integer, ForeignKey('cluster.id_cluster'))
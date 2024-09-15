from sqlalchemy import Column, Integer, String
from .database import Base

class Seccion(Base):
    __tablename__ = 'seccion'
    
    id_seccion = Column(Integer, primary_key=True, index=True)
    nombre_seccion = Column(String(100), nullable=False)

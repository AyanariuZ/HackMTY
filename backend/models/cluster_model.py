from sqlalchemy import Column, Integer, String
from .database import Base

class Cluster(Base):
    __tablename__ = 'cluster'
    
    id_cluster = Column(Integer, primary_key=True, index=True)
    nombre_cluster = Column(String(100), nullable=False)
    descripcion_cluster = Column(String(255))

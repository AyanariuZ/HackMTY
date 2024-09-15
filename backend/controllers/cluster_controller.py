from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.database import SessionLocal
from ..models.cluster_model import Cluster
from ..schemas.cluster_schema import ClusterSchema

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todos los clusters
@router.get("/clusters", response_model=list[ClusterSchema])
def get_clusters(db: Session = Depends(get_db)):
    clusters = db.query(Cluster).all()
    return clusters

# Obtener un cluster por su ID
@router.get("/clusters/{cluster_id}", response_model=ClusterSchema)
def get_cluster(cluster_id: int, db: Session = Depends(get_db)):
    cluster = db.query(Cluster).filter(Cluster.id_cluster == cluster_id).first()
    if cluster is None:
        raise HTTPException(status_code=404, detail="Cluster not found")
    return cluster

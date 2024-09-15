from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.database import SessionLocal
from ..models.seccion_model import Seccion
from ..schemas.seccion_schema import SeccionSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todas las secciones
@router.get("/secciones", response_model=list[SeccionSchema])
def get_secciones(db: Session = Depends(get_db)):
    secciones = db.query(Seccion).all()
    return secciones

# Obtener una seccion por su ID
@router.get("/secciones/{seccion_id}", response_model=SeccionSchema)
def get_seccion(seccion_id: int, db: Session = Depends(get_db)):
    seccion = db.query(Seccion).filter(Seccion.id_seccion == seccion_id).first()
    if seccion is None:
        raise HTTPException(status_code=404, detail="Seccion not found")
    return seccion

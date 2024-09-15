from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.database import SessionLocal
from ..models.visita_model import Visita
from ..schemas.visita_schema import VisitaSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todas las visitas
@router.get("/visitas", response_model=list[VisitaSchema])
def get_visitas(db: Session = Depends(get_db)):
    visitas = db.query(Visita).all()
    return visitas

# Obtener una visita por su ID
@router.get("/visitas/{visita_id}", response_model=VisitaSchema)
def get_visita(visita_id: int, db: Session = Depends(get_db)):
    visita = db.query(Visita).filter(Visita.id_visita == visita_id).first()
    if visita is None:
        raise HTTPException(status_code=404, detail="Visita not found")
    return visita

@router.post("/visita/", response_model=VisitaSchema)
def create_visita(visita: VisitaSchema, db: Session = Depends(get_db)):
    db_visita = Visita(**visita.dict())
    db.add(db_visita)
    db.commit()
    db.refresh(db_visita)
    return db_visita
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.database import SessionLocal
from ..models.promocion_model import Promocion
from ..schemas.promocion_schema import PromocionSchema
from ..schemas.promocion_patch_schema import PromocionPatchSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todas las promociones
@router.get("/promociones", response_model=list[PromocionSchema])
def get_promociones(db: Session = Depends(get_db)):
    promociones = db.query(Promocion).all()
    return promociones

# Obtener una promocion por su ID
@router.get("/promociones/{promocion_id}", response_model=PromocionSchema)
def get_promocion(promocion_id: int, db: Session = Depends(get_db)):
    promocion = db.query(Promocion).filter(Promocion.id_promocion == promocion_id).first()
    if promocion is None:
        raise HTTPException(status_code=404, detail="Promocion not found")
    return promocion

@router.post("/promocion/", response_model=PromocionSchema)
def create_promocion(promocion: PromocionSchema, db: Session = Depends(get_db)):
    db_promocion = Promocion(**promocion.dict())
    db.add(db_promocion)
    db.commit()
    db.refresh(db_promocion)
    return db_promocion


# PATCH para la tabla promocion
@router.patch("/promocion/{id_promocion}")
def patch_promocion(id_promocion: int, promocion_data: PromocionPatchSchema, db: Session = Depends(get_db)):
    promocion = db.query(Promocion).filter(Promocion.id_promocion == id_promocion).first()
    
    if not promocion:
        raise HTTPException(status_code=404, detail="Promoción no encontrada")
    
    # Actualización parcial de la promoción
    update_data = promocion_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(promocion, key, value)
    
    db.commit()
    db.refresh(promocion)
    return promocion
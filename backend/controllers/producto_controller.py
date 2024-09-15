from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.database import SessionLocal
from ..models.producto_model import Producto
from ..schemas.producto_schema import ProductoSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todos los productos
@router.get("/productos", response_model=list[ProductoSchema])
def get_productos(db: Session = Depends(get_db)):
    productos = db.query(Producto).all()
    return productos

# Obtener un producto por su ID
@router.get("/productos/{producto_id}", response_model=ProductoSchema)
def get_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id_producto == producto_id).first()
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return producto

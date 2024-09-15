from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.database import SessionLocal
from ..models.cliente_model import Cliente
from ..schemas.cliente_schema import ClienteSchema
from ..schemas.cliente_patch_schema import ClientePatchSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todos los clientes
@router.get("/clientes", response_model=list[ClienteSchema])
def get_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    return clientes

# Obtener un cliente por su ID
@router.get("/clientes/{cliente_id}", response_model=ClienteSchema)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id_cliente == cliente_id).first()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return cliente

@router.post("/cliente/", response_model=ClienteSchema)
def create_cliente(cliente: ClienteSchema, db: Session = Depends(get_db)):
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


# PATCH para la tabla cliente
@router.patch("/cliente/{id_cliente}")
def patch_cliente(id_cliente: int, cliente_data: ClientePatchSchema, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()
    
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    # Actualización parcial del cliente
    update_data = cliente_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(cliente, key, value)
    
    db.commit()
    db.refresh(cliente)
    return cliente
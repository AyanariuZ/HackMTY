from pydantic import BaseModel

class ProductoSchema(BaseModel):
    id_producto: int
    imagen: str
    nombre_producto: str
    precio: int
    id_seccion: int

    class Config:
        from_attributes = True

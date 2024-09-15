from pydantic import BaseModel

class PromocionSchema(BaseModel):
    id_cliente: int
    titulo: str
    descripcion_promocion: str
    aceptado: int  # 1 para aceptado, 0 para rechazado

    class Config:
        from_attributes = True

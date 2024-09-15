from pydantic import BaseModel
from datetime import date

class VisitaSchema(BaseModel):
    id_cliente: int
    fecha: date

    class Config:
        from_attributes = True

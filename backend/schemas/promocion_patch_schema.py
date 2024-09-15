from pydantic import BaseModel
from typing import Optional

class PromocionPatchSchema(BaseModel):
    titulo: Optional[str] = None
    descripcion_promocion: Optional[str] = None
    aceptado: Optional[int] = None

    class Config:
        from_attributes = True

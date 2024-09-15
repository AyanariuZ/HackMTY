from pydantic import BaseModel
from typing import Optional

class ClientePatchSchema(BaseModel):
    edad: Optional[int] = None
    sexo: Optional[int] = None
    id_cluster: Optional[int] = None

    class Config:
        from_attributes = True

from pydantic import BaseModel

class SeccionSchema(BaseModel):
    id_seccion: int
    nombre_seccion: str

    class Config:
        from_attributes = True

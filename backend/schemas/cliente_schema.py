from pydantic import BaseModel

class ClienteSchema(BaseModel):
    edad: int
    sexo: int  # 0 para mujer, 1 para hombre
    id_cluster: int

    class Config:
        from_attributes = True

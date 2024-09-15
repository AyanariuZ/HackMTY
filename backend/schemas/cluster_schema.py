from pydantic import BaseModel

class ClusterSchema(BaseModel):
    id_cluster: int
    nombre_cluster: str
    descripcion_cluster: str

    class Config:
        from_attributes = True

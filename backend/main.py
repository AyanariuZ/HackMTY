from fastapi import FastAPI
from .controllers import cluster_controller, cliente_controller, visita_controller, seccion_controller, producto_controller, promocion_controller

app = FastAPI()

# Incluir los controladores (routers)
app.include_router(cluster_controller.router)
app.include_router(cliente_controller.router)
app.include_router(visita_controller.router)
app.include_router(seccion_controller.router)
app.include_router(producto_controller.router)
app.include_router(promocion_controller.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)

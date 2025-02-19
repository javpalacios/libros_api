from fastapi import FastAPI
from app.routes import libros, autores
from app.db.session import engine
from sqlmodel import SQLModel

app = FastAPI()

# Registrar las rutas
app.include_router(autores.router)
app.include_router(libros.router)

# Crear tablas en la base de datos si no existen
def init_db():
    SQLModel.metadata.create_all(engine)

init_db()

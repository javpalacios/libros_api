from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Libro(SQLModel, table=True):
    titulo: str
    isbn: str
    anio: int | None = None
    genero: str | None = None
    sinopsis: str | None = None
    portada_uri: str | None = None
    autor_id: int = Field(foreign_key="autor.id")

    id: int | None = Field(default=None, primary_key=True)
    autor: Optional["Autor"] = Relationship(back_populates="libros")

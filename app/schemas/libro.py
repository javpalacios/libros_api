from sqlmodel import SQLModel

class LibroCreate(SQLModel):
    titulo: str
    isbn: str
    anio: int | None = None
    autor_id: int
    genero: str | None = None
    sinopsis: str | None = None
    portada_uri: str | None = None

class LibroResponse(LibroCreate):
    id: int

class LibroUpdate(SQLModel):
    titulo: str | None = None
    isbn: str | None = None
    anio: int | None = None
    genero: str | None = None
    sinopsis: str | None = None
    portada_uri: str | None = None
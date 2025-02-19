from sqlmodel import SQLModel

class AutorCreate(SQLModel):
    nombre: str
    fecha_nacimiento: int | None = None
    nacionalidad: str | None = None
    biografía: str | None = None
    fotografia_uri: str | None = None

class AutorResponse(AutorCreate):
    id: int

class AutorUpdate(SQLModel):
    nombre: str | None = None
    fecha_nacimiento: int | None = None
    nacionalidad: str | None = None
    biografía: str | None = None
    fotografia_uri: str | None = None
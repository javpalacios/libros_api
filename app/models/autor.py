from sqlmodel import SQLModel, Field, Relationship

class Autor(SQLModel, table=True):
    nombre: str | None = None
    fecha_nacimiento: int | None = None
    nacionalidad: str | None = None
    biografía: str | None = None
    fotografia_uri: str | None = None

    id: int | None = Field(default=None, primary_key=True)
    libros: list["Libro"] = Relationship(back_populates="autor", cascade_delete=True)

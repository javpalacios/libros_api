from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.libro import Libro
from app.schemas.libro import LibroCreate, LibroResponse, LibroUpdate
from app.db.session import get_session

class LibroService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, libro_data: LibroCreate) -> LibroResponse:
        libro = Libro(**libro_data.model_dump())
        self.session.add(libro)
        self.session.commit()
        self.session.refresh(libro)
        return LibroResponse(**libro.model_dump())

    def get_all(self, autor_id: int | None, anio: int | None, genero: str | None):
        query = select(Libro)

        if autor_id:
            query = query.where(Libro.autor_id == autor_id)
        if anio:
            query = query.where(Libro.anio == anio)
        if genero:
            query = query.where(Libro.genero == genero)

        return self.session.exec(query).all()

    def get_by_id(self, id: int):
        return self.session.get(Libro, id)

    def update(self, id: int, libro_data: LibroUpdate) -> Libro:
        libro = self.session.get(Libro, id)
        if not libro:
            raise HTTPException(status_code=404, detail="Libro no encontrado")

        libro_dict = libro_data.model_dump(exclude_unset=True)
        for key, value in libro_dict.items():
            setattr(libro, key, value)

        self.session.add(libro)
        self.session.commit()
        self.session.refresh(libro)
        return libro

    def delete(self, id: int):
        libro = self.session.get(Libro, id)
        if not libro:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        self.session.delete(libro)
        self.session.commit()
        return {"message": "Libro eliminado"}

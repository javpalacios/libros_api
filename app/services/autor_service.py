from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.autor import Autor
from app.schemas.autor import AutorCreate, AutorResponse, AutorUpdate
from app.db.session import get_session

class AutorService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_autor(self, autor_data: AutorCreate) -> AutorResponse:
        autor = Autor(**autor_data.model_dump())
        self.session.add(autor)
        self.session.commit()
        self.session.refresh(autor)
        return AutorResponse(**autor.model_dump())

    def get_all_autores(self):
        return self.session.exec(select(Autor)).all()

    def get_autor_by_id(self, id: int):
        return self.session.get(Autor, id)
    
    def update_autor(self, id: int, autor_data: AutorUpdate) -> Autor:
        autor = self.session.get(Autor, id)
        if not autor:
            raise HTTPException(status_code=404, detail="Autor no encontrado")

        autor_dict = autor_data.model_dump(exclude_unset=True)
        for key, value in autor_dict.items():
            setattr(autor, key, value)

        self.session.add(autor)
        self.session.commit()
        self.session.refresh(autor)
        return autor
    
    def delete_autor(self, id: int):
        autor = self.session.get(Autor, id)
        if not autor:
            raise HTTPException(status_code=404, detail="Autor no encontrado")
        self.session.delete(autor)
        self.session.commit()
        return {"message": "Autor eliminado exitosamente"}

from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.services.autor_service import AutorService
from app.schemas.autor import AutorCreate, AutorResponse, AutorUpdate

router = APIRouter(prefix="/autores", tags=["Autores"])

@router.post("/", response_model=AutorResponse)
def create_autor(autor: AutorCreate, service: AutorService = Depends()):
    return service.create(autor)

@router.get("/", response_model=list[AutorResponse])
def read_autores(service: AutorService = Depends()):
    return service.get_all()

@router.get("/{id}", response_model=AutorResponse)
def read_autor(id: int, service: AutorService = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model=AutorResponse)
def update_autor(id: int, autor_data: AutorUpdate, service: AutorService = Depends()):
    return service.update(id, autor_data)

@router.delete("/{id}", response_model=dict)
async def delete_autor(id: int, service: AutorService = Depends()):
    return service.delete(id)

from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db.session import get_session
from app.services.autor_service import AutorService
from app.schemas.autor import AutorCreate, AutorResponse, AutorUpdate

router = APIRouter(prefix="/autores", tags=["Autores"])

@router.post("/", response_model=AutorResponse)
def agregar_autor(autor: AutorCreate, service: AutorService = Depends()):
    return service.create_autor(autor)

@router.get("/", response_model=list[AutorResponse])
def obtener_autores(service: AutorService = Depends()):
    return service.get_all_autores()

@router.get("/{id}", response_model=AutorResponse)
def obtener_autor(id: int, service: AutorService = Depends()):
    return service.get_autor_by_id(id)

@router.patch("/{id}", response_model=AutorResponse)
def update_autor(id: int, autor_data: AutorUpdate, service: AutorService = Depends()):
    return service.update_autor(id, autor_data)

@router.delete("/{id}", response_model=dict)
async def delete_autor(id: int, service: AutorService = Depends()):
    return service.delete_autor(id)

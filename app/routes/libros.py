from fastapi import APIRouter, Depends, Query
from app.services.libro_service import LibroService
from app.schemas.libro import LibroCreate, LibroResponse, LibroUpdate

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/", response_model=LibroResponse)
def create_libro(libro: LibroCreate, service: LibroService = Depends()):
    return service.create_libro(libro)

@router.get("/", response_model=list[LibroResponse])
def read_libros(service: LibroService = Depends(),
    autor_id: int | None = Query(None, description="Filtrar por ID del autor"),
    anio: int | None = Query(None, description="Filtrar por año de publicación"),
    genero: str | None = Query(None, description="Filtrar por género")):
    return service.get_all_libros(autor_id, anio, genero)

@router.get("/{id}", response_model=LibroResponse)
def read_libro(id: int, service: LibroService = Depends()):
    return service.get_libro_by_id(id)

@router.patch("/{id}", response_model=LibroResponse)
def update_libro(id: int, libro_data: LibroUpdate, service: LibroService = Depends()):
    return service.update_libro(id, libro_data)

@router.delete("/{id}", response_model=dict)
async def delete_libro(id: int, service: LibroService = Depends()):
    return service.delete_libro(id)

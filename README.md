# LibrosAPI
## API de FastAPI con SQLModel
Ejemplo de una API para gestionar Autores y Libros con una base de datos SQLite.

### Construir la imagen de Docker
En el directorio raíz de tu proyecto (donde se encuentra el archivo `Dockerfile`), ejecuta el siguiente comando para construir la imagen Docker:
```bash
docker build -t libros_api .
```


### Ejecutar el contenedor Docker
Utilizando sqlite:
```bash
docker run -d -p 8000:8000 libros_api
```
Utilizando otra bbdd:
```bash
docker run -d -p -e DATABASE_URL="postgres://postgres:123456@127.0.0.1:5432/dummy" 8000:8000 libros_api
```

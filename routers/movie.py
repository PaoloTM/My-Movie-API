from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import  Session
from models.movie import Movie as MovieModel #para evitar confusiones con la clase Movie ya existente
from middlewares.jwt_bearer import JWTBearer #añadimos el middleware de login
from fastapi.encoders import jsonable_encoder #trasnforma los datos a un json legible
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())]) 
def get_movies() -> List[Movie]:
    db = Session() #guardamos el iniciador de sesiones en una variable para poder insertar,eliminar,modificar en la BD
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result)) #transformamos los datos de moviemodel a un json legible con jsonable_encoder

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=404)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session() #guardamos el iniciador de sesiones en una variable para poder insertar,eliminar,modificar en la BD
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "ID no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
        

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=404)
def get_movies_by_category(category: str = Query(min_length=5, max_length=20)) -> List[Movie]:
    db = Session() #guardamos el iniciador de sesiones en una variable para poder insertar,eliminar,modificar en la BD
    result = MovieService(db).get_movie_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Categoria no encontrada"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movies(movie: Movie) -> dict:
    db = Session() #guardamos el iniciador de sesiones en una variable para poder insertar,eliminar,modificar en la BD
    MovieService(db).create_movie(movie) #llamamos a la funcion movieservice para iniciar la bd y la funcion create movie insertamos los datos que el usuario paso a la bd
    return JSONResponse(status_code=201, content={"message": "Se registro exitosamente la pelicula"})

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session() #guardamos el iniciador de sesiones en una variable para poder insertar,eliminar,modificar en la BD
    result = MovieService(db).get_movie(id) #corroboramos que el id exista con get_movie
    if not result:
        return JSONResponse(status_code=404, content={'message': "ID no encontrado"})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Se edito exitosamente la pelicula"})

@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    db = Session() #guardamos el iniciador de sesiones en una variable para poder insertar,eliminar,modificar en la BD
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "ID no encontrado"})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se elimino exitosamente la pelicula"})
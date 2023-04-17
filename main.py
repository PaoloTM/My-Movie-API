from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler #añadiremos un middleware a nuestra aplicacion
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler) #añadimos el middleware a nivel general de la aplicacion

#incluimos los routers a nuestro programa principal / es una manera de tener todo mas ordenado x carpetas
app.include_router(movie_router)
app.include_router(user_router)


#crea todas las tablas definidas en nuestras clases ORM, y con bind especificamos el motor a utilizar para crear esas tablas
Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')
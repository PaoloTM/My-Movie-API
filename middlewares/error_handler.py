from starlette.middleware.base import BaseHTTPMiddleware #el modulo sirve para implemetar middlewares a nuestra aplicacion
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse

class ErrorHandler(BaseHTTPMiddleware):
    # __init__ se utiliza para iniciar la instancia del middleware
    def __init__(self, app: FastAPI) -> None: #self se refiere a la instancia actual de la clase = a this en js, -> solo indifca el tipo de dato que va a devolver la funcion es una buena practica indicarlo
        super().__init__(app)
    
    #dispatch se encarga de enrutar la solicitud
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse: #callnext llama al siguiente middleware si el primero se ejecuto de manera satisfactoria
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})
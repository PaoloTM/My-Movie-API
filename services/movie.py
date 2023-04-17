from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():

    def __init__(self, db) -> None:
        self.db = db
    
    def get_movies(self):
        result = self.db.query(MovieModel).all() #obtenemos todos los datos de la tabla moviemodel
        return result
    
    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first() #obtenemos los datos solicitados solo si se cumple el filtrado por id y lo guardamos en la variable
        return result
    
    def get_movie_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all() #obtenemos los datos solicitados solo si se cumple el filtrado por categoria y lo guardamos en la variable, el metodo all es para obtener todos los datos que cumplan la condicion
        return result
    
    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict()) #a moviemodel le vamos a pasar el parametro de la clase movie convertido a dict para extraer sus atributos con ** y extraer los parametros
        self.db.add(new_movie) #agregamos los datos que le pasamos a los parametros de movie a nuestra base de datos
        self.db.commit() #actualizamos la base de datos para que los datos se guarden
        return
    
    def update_movie(self, id: int, data: Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first() #obtenemos los datos solicitados solo si se cumple el filtrado por id y lo guardamos en la variable
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit() #actualizamos la base de datos para que los datos se guarden
        return
    
    def delete_movie(self, id: int):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first() #obtenemos los datos solicitados solo si se cumple el filtrado por id y lo guardamos en la variable
        self.db.delete(result) #eliminamos el resultado de la base de datos
        self.db.commit() #actualizamos la base de datos para que los datos se guarden
        return 

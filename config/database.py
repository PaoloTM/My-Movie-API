import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#este es el nombre del archivo que creara sqlalchemy al ejecutarse y donde lo guardara
sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__)) #obtenemos la ruta absoluta del directorio que contiene el archivo python actual

#con f".." le damos formato a nuestro texto que serviria para agregar variables
#sqlite:/// sirve para conectar nuestra base de datos y darle una url
#con os.path.join unimos 2 parametros necesarios la ruta de mi base de datos y el nombre
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

#create engine es el encargado de establecer la conexion con nuestra base de datos y el parametro echo sirve para que me muestre x consola lo que se realiza en cada momento
engine = create_engine(database_url, echo=True)

#sessionmaker es una clase que nos permite crear una sesion personalizada para interactuar con nuestra base de datos y especificamos la conexion a esa BD con el parametro bind
Session = sessionmaker(bind=engine)

#esta funcion nos permite crear una clase base personalizada para definir nuestras propias clases ORM, asi interactuar con la base de datos utilizando objetos python en lugar de sentencias SQL
Base = declarative_base()

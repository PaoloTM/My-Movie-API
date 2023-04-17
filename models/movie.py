from config.database import Base
from sqlalchemy import Column, Integer, String, Float

#la clase movie heredara Base para que asi se pueda definir como una clase ORM y utlizar estructuras de base de datos, con esto ya se puede interactuar con la misma
class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
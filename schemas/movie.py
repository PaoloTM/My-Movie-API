from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: int | None = None
    title: str = Field(min_length=4, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(lt=10)
    category: str = Field(min_length=5, max_length=20)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi Pelicula",
                "overview": "Descripcion de la Pelicula",
                "year": 2023,
                "rating": 7.1,
                "category": "Accion"
            }
        }

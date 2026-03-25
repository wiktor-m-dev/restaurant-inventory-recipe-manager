import re
from pydantic import BaseModel, field_validator

class Supplier(BaseModel):
    id: int
    name: str
    email: str

    @field_validator('email')
    @classmethod
    def check_email(cls, value: str) -> str:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError('Nieprawidłowy format adresu email')
        return value

class Ingredient(BaseModel):
    id: int
    name: str
    stock_level: int
    supplier_id: int

    @field_validator('stock_level')
    @classmethod
    def check_stock(cls, value: int) -> int:
        if value < 0:
            raise ValueError('Poziom zapasów nie może spaść poniżej 0')
        return value

class Recipe(BaseModel):
    id: int
    name: str
    prep_time_mins: int
    
    @field_validator('prep_time_mins')
    @classmethod
    def check_prep_time(cls, value: int) -> int:
        if value <= 0:
            raise ValueError('Czas przygotowania musi być większy niż 0 minut')
        return value
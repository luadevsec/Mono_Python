from pydantic import BaseModel
from typing import Optional
class PlanoA(BaseModel):
    nome: str = 'starter'
    min: float = 200.0
    earn: float = 0.5  # Porcentagem de lucro por dia
    time: int = 90  # Tempo em dias para o saque

class PlanoB(BaseModel):
    nome: str = 'silver'
    min: float = 500.0
    earn: float = 0.5
    time: int = 60

class PlanoC(BaseModel):
    nome: str = 'golden'
    min: float = 500.0
    earn: float = 0.5
    time: int = 60

class PlanoD(BaseModel):
    nome: str = 'diamond'
    min: float = 500.0
    earn: float = 0.5
    time: int = 30

class PlanoF(BaseModel):
    nome: str = 'personalite'
    min: float = 1000.0
    earn: float = 0.8
    time: int = 10


class Usuario(BaseModel):
    nome: str
    senha: str
    money: Optional[float] = 0
    date: Optional[str] = None 
    plano: Optional[str] = None
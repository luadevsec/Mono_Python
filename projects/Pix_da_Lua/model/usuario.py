from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    def __init__(
            self, 
            nome: str,
            senha: str = '1234',
            money: Optional[float] = 0,
            date: Optional[str] = None):
        self.nome = nome
        self.senha = senha
        self.money = money
        self.date = date
        self.plano = None


sqlalchemy.
sqlite

sqlitebrowser


tinydb
mongodb

from fastapi import FastAPI
app = FastAPI()

################################################################ MODELS
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



# ... (definição das rotas)
from fastapi import APIRouter


router = APIRouter()
@router.get('/planos', tags={'getsS'})
def get_plano(plano: int = 0):
    plano = int(plano)
    if plano == 1:
        return {'stats': 200, 'plano': PlanoA()}
    elif plano == 2:
        return {'stats': 200, 'plano': PlanoB()}
    elif plano == 3:
        return {'stats': 200, 'plano': PlanoC()}
    elif plano == 4:
        return {'stats': 200, 'plano': PlanoD()}
    elif plano == 5:
        return {'stats': 200, 'plano': PlanoF()}
    elif plano == 0:
        return {'stats': 200, 'planos': [PlanoA(), PlanoB(), PlanoC(), PlanoD(), PlanoF()]}
    else:
        return {'stats': 404}

@router.get('/usuarios')
async def get_usuarios(nome: str = 'Lua', senha: str = '1234'):
    return {'stats': 200, 'model': Usuario(nome = nome, senha = senha)}


app.include_router(router)



if __name__ == '__main__': 
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)
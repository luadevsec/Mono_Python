from fastapi import APIRouter
from models.planos import PlanoA, PlanoB, PlanoC, PlanoD, PlanoF

planos_router = APIRouter()

@planos_router.get('/planos')
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
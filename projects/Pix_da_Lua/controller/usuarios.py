from fastapi import APIRouter

usuarios_router = APIRouter()

@usuarios_router.get('/usuarios')
async def get_usuarios():
    return {'stats': 200}
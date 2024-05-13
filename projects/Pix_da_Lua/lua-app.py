from fastapi import FastAPI
from rotas.planos import planos_router
from rotas.usuarios import usuarios_router

app = FastAPI()


#rotas
app.include_router(usuarios_router)
app.include_router(planos_router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)
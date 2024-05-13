from rotas import rotas
from fastapi import FastAPI

app = FastAPI()
app.include_router(rotas)







import subprocess
def start_server():
    command = [
        "uvicorn",
        "app:app",
        "--host", "localhost",
        "--port", "7777",
        "--reload"
    ]
    
    subprocess.run(command)
if __name__ == "__main__":
    start_server()


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista para almacenar usuarios
users = []

# Modelo de usuario
class User(BaseModel):
    name: str
    age: int
    email: str

# Endpoint para agregar usuario
# Endpoint para obtener usuarios
@app.get("/users/")
def get_users():
    return {"users": users}

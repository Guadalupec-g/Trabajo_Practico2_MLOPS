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
@app.post("/users/")
def add_user(user: User):
    users.append(user)
    return {"message": "Usuario agregado correctamente", "user": user}

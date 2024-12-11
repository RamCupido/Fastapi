from fastapi import FastAPI
from pydantic import BaseModel

# Se crear la aplicación FastAPI
app = FastAPI()

#Clase para crear un usuario con varios parametros
class User(BaseModel):
    id: str
    email: str
    age: int
    is_admin: bool

#Metodo sin parametros
@app.get("/")
def root():
    #Retorna el mensaje que nostros queramos en formato JSON
    return { "mensaje" : "Hola Mundo"}

#Metodo que tiene parametros como el id y el cat
@app.get("/users/{cat}")
def get_users (id: int, cat):
    #Retorna el id de tipo int y el cat (JSON)
    return {"id": id, "cat": cat}

#Metodo que ingresa 1 usuario
@app.post("/users")
def save_users(user: User):
    return user
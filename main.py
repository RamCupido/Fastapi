import uvicorn
from fastapi import FastAPI

# Se crear la aplicación FastAPI
app = FastAPI()

@app.get("/")
def index():
    #Retorna el mensaje que nostros queramos
    return { "mensaje" : "Hola Mundo"}

if __name__ == "__main__":
    #Inicia el servidor de FastAPI con Uvicorn
    uvicorn.run("main:app", port=8000, reload=True)

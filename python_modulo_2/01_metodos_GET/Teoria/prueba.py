# primera ejecucion:EJECUTAR EN LA TERMINAL: uvicorn main:app --reload

# Segunda ejecución: uvicorn 01_metodos_GET.prueba:app --reload

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# ME SALE ERROR EN LA SEGUNDA EJECUCION


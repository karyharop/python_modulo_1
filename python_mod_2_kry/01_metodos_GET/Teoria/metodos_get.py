"""
El metodo GET, sirve para obtener datos (traer datos)
Es el más simple y común de todos.

- importa FastAPI para crear nuestra aplicacion
 """
from fastapi import FastAPI

"""
    - Creamos la instancia de nuestra aplicacion FastAPI
    - Esta instancia debe crearse una sola vez al inicio del archivo

"""

app = FastAPI()

"""
- Creamos la ruta raíz ("/")
- El decorador @app.get("/"), le dice a FastAPI cuando alguien visite la ruta raíz ("/"),
tiene que ejecutar la ruta raíz.
"""

@app.get("/")
def leer_raiz():
    # devolvemos un diccionario y FasAPI lo convierte en JSON.
    return {"mensaje": "¡Hola desde la ruta raíz!"}

@app.get("/inicio")
def obtener_informacion():
    return{"autor": "La grajilla", "descripción": "API molona de ejemplo para explicar en clases", "fecha": "2025- 10-24"}

# NO ME FUNCIONA LOCALHOST!!!


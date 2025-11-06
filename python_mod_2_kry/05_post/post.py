"""
- async es una funcion que sirve para que nuestro programa 
pueda hacer varias cosas a la vez.
- para mejorar el rendimiento. tb llamada programacion asincrona
- es muy útil en programaciones muy grandes.
- permite que mientras se está realizando alguna accion tb se realice otra.
usuario minuscula: variable de esa funcion
usuario mayuscula:variable de tipo usuario que va a ser yipo de dato (clase)
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int

@app.post("/usuarios")
async def crear_usuario(usuario: Usuario):
    return {
        "mensaje": f"Usuario {usuario.nombre} creado con éxito",
        "datos": {
            "nombre": usuario.nombre,
            "email": usuario.email,
            "edad": usuario.edad
        }
    }

class Contacto(BaseModel):
    nombre: str
    telefono: str
    email: str

@app.post("/contactos")
async def crear_contacto(contacto: Contacto):
    respuesta = f"Gracias {contacto.nombre}, hemos enviado la confirmación al email {contacto.email}"
    return {"respuesta": respuesta}



"""
Crea un endpoint en FastAPI que permita obtener información 
de un usuario específico utilizando tanto path parameters 
como query parameters.

Debes crear:

Un endpoint con la ruta /users/{user_id} 
donde user_id es un path parameter de tipo entero
El endpoint debe aceptar dos query parameters opcionales:
include_email: booleano con valor por defecto False
format: string con valor por defecto "basic"
La función debe devolver un diccionario con:
user_id: el ID del usuario recibido como path parameter
name: un string que diga "Usuario {user_id}"
email: solo si include_email es True, devolver "user{user_id}@example.com"
format: el valor del query parameter format recibido
Para empezar, importa FastAPI, crea la instancia de la 
aplicación con app = FastAPI(), y define tu función con el 
decorador @app.get() especificando la ruta correcta. 
Recuerda que los path parameters se indican con 
llaves {} en la ruta y los query parameters son parámetros 
adicionales de la función con valores por defecto. 
    
"""
# primer ejercicio

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int, include_email: bool = False, format: str = "basic"):
    user_data = {
        "user_id": user_id,
        "format": format      
    }
    # añadir email si include_email es true
    if include_email:
        user_data["email"] = f"user{user_id}@example.com"
        
    return user_data

"""
Crea un endpoint en FastAPI que permita obtener información 
de productos específicos utilizando tanto path parameters 
como query parameters.

Debes crear:

1. Un endpoint con la ruta /products/{product_id} 
donde product_id es un path parameter de tipo entero  

2. El endpoint debe aceptar tres query parameters opcionales:

include_price: booleano con valor por defecto False
include_stock: booleano con valor por defecto False
format: string con valor por defecto "summary"
3. La función debe devolver un diccionario con:

product_id: el ID del producto recibido como path parameter
name: un string que diga "Producto {product_id}"
category: un string que diga "Categoría {product_id % 3 + 1}" 
(esto dará categorías 1, 2 o 3)
price: solo si include_price es True, devolver un precio 
calculado como {product_id * 10}.99
stock: solo si include_stock es True, devolver un stock c
alculado como {product_id * 5}
format: el valor del query parameter format recibido
"""

# Segundo ejercicio

from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{product_id}")
def get_products(product_id: int, include_price: bool = False, include_stock: bool = False, format: str = "summary"):
    product_data = {
        # Crear diccionario con datos básicos
        "product_id": product_id, 
        "name": f"Producto {product_id}",
        "category": f"Categoría {product_id % 3 + 1}",
        "format": format    
    }

    # añadir precio si include_price es true
    if include_price:
        product_data["price"] = f"{product_id * 10}.99"
    #añadir stock si include_stock es true
    if include_stock:
        product_data["stock"] = product_id * 5



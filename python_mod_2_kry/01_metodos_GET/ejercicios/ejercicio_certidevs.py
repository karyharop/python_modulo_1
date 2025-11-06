# RETO- CERTIDEVS

from fastapi import FastAPI


# Crear la instancia de la aplicación
app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"mensaje": "Vamos a ver los tipos de datos"}

@app.get("/animales")
def obtener_animales():
    return {"animales": ["Leon", "Jirafa", "Antílope", "Cebra"],        
                
    }

# Escribe aquí tu código para los endpoints GET

@app.get("/zoologico")
def obtener_zoologico():
    return { "nombre": "ZOOLÓGICO_ALMAS", 
            "cantidad_animales": 16, 
            "abierto": True, 
            "horario": "10-16" 
    }
    
@app.get("/estadisticas")
def obtener_estadisticas():
    return {"Informacion_general": {
        "Nombre": "ZOOLÓGICO_ALMAS",
        "Ubicacion": "Cabanillas de la Sierra",
    },
        "Datos_animales": {
        "Total_especies": 4,
        "Animales_populares": ["Jirafa", "Leon"]
    },
        "Estado_operacional": {
        "Abierto": True,
        "Empleados_presentes": 5
    }            
   }            
            
 # hay que colocar en la terminal: uvicorn 01_metodos_GET.respuestas_dinamicas:app --reload          
            
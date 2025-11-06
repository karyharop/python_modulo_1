"""
Crea una aplicación FastAPI para un consultorio médico con los siguientes componentes:

1. Modelos Pydantic requeridos:

Modelo Contacto con campos:

telefono: string (obligatorio)
email: string (opcional, puede ser None)
Modelo Paciente con campos:

nombre: string (obligatorio)
apellido: string (obligatorio)
edad: entero (obligatorio)
contacto: objeto Contacto (obligatorio)
alergias: lista de strings (opcional, lista vacía por defecto)
activo: boolean (opcional, valor por defecto True)

2. Endpoints requeridos:

POST /pacientes: Registra un nuevo paciente
GET /pacientes: Devuelve lista de todos los pacientes
GET /pacientes/{paciente_id}: Devuelve un paciente específico
GET /pacientes/activos: Devuelve solo pacientes activos
3. Funcionalidades específicas:

Usa una lista en memoria para almacenar pacientes
Genera IDs automáticamente (empezando en 1)
El POST debe devolver confirmación con el ID generado
Los GET deben mostrar información estructurada
Ejemplo de uso:

POST /pacientes con:
{
  "nombre": "Carlos",
  "apellido": "Rodríguez",
  "edad": 28,
  "contacto": {
    "telefono": "123 45 67 89",
    "email": "carlos@email.com"
  },
  "alergias": ["penicilina"]
}
respuesta esperada:
{
  "id": 1,
  "mensaje": "Paciente Carlos Rodríguez registrado exitosamente",
  "paciente": {
    "nombre": "Carlos",
    "apellido": "Rodríguez",
    "edad": 28,
    "telefono": "123 45 67 89",
    "tiene_alergias": true
  }
}
GET/pacientes debe devolver:

{
  "pacientes": [
    {
      "id": 1,
      "nombre": "Carlos",
      "apellido": "Rodríguez",
      "edad": 28,
      "activo": true
    }
  ],
  "total": 1
}

GET/ pacientes/1 debe devolver:
{
  "id": 1,
  "nombre": "Carlos",
  "apellido": "Rodríguez",
  "edad": 28,
  "contacto": {
    "telefono": "123 45 67 89",
    "email": "carlos@email.com"
  },
  "alergias": ["penicilina"],
  "activo": true
}
GET/pacientes/activos debe devolver:
{
  "pacientes_activos": [
    {
      "id": 1,
      "nombre_completo": "Carlos Rodríguez",
      "edad": 28,
      "telefono": "123 45 67 89"
    }
  ],
  "cantidad": 1
}

"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# lista vacía para guardar pacientes
pacientes_db = []

# contador para IDs
contador_id = 1
# definiendo el modelo de contacto
class Contacto(BaseModel):
    telefono: str
    email: Optional[str] = None
# definiendo el modelo para pacientes, heredado de basemodel 
# para ahorrar constructor y otros

class Paciente(BaseModel):
    nombre: str
    apellido: str
    edad: int
    contacto: Contacto
    alergias: List[str] = []
    activo: bool = True
    
# sirve para registrat nuevos pacientes, a través del metodo post
@app.post("/pacientes")
def registrar_paciente(paciente: Paciente):
    # declarar que vamos a usar una variable global, esto es para poder
    # usar la variable que habiamos creado de contador_id fuera de la funcion
    global contador_id
    
    # convertir objeto paciente a diccionario
    paciente_data = paciente.model_dump()
    
    # asignar id al paciente
    paciente_data["id"] = contador_id
    
    # añadir pacienta a base de datos
    pacientes_db.append(paciente_data)
    
    # comprobar si paciente tiene alergias, estamos preguntando 
    # si es una lista vacia o no
    tiene_alergias = len(paciente.alergias) > 0
    
    response = {
        "id": contador_id,
        "mensaje": f"Paciente {paciente.nombre} {paciente.apellido} registrado existosamente",
        "paciente": {
            "nombre": paciente.nombre,
            "apellido": paciente.apellido,
            "edad": paciente.edad,
            "telefono": paciente.contacto.telefono,
            "tiene_alergias": tiene_alergias
        }
    }
    
    # incrementar contador de id, se sumará 1 cada vez que se ejecute lo anterior
    contador_id += 1
    
    return response

@app.get("/pacientes")
def listar_pacientes():
    # lista con información, cada elemento de nuestra lista se llamará p
    pacientes_resumen = [
        {
            "id": p["id"],
            "nombre": p["nombre"],
            "apellido": p["apellido"],
            "edad": p["edad"],
            "activo": p["activo"]
        }
        for p in pacientes_db
    ]
    
    return {
        "pacientes": pacientes_resumen,
        "total": len(pacientes_resumen)
    }

@app.get("/pacientes/activos")
def obtener_pacientes_activos():
    pacientes_activos = [
        {
            "id": p["id"],
            "nombre_completo": f"{p["nombre"]} {p["apellido"]}",
            "edad": p["edad"],
            "telefono": p["contacto"]["telefono"]
        }
        for p in pacientes_db if p["activo"]
    ]
    
    return {
        "pacientes_activos": pacientes_activos,
        "cantidad": len(pacientes_activos)
    }

# los métodos dinámicos (los que tengan parámetros de ruta como {paciente_id}) siempre ponerlos al final
@app.get("/pacientes/{paciente_id}")
def obtener_paciente(paciente_id: int):
    for p in pacientes_db:
        if p["id"] == paciente_id:
            return p
    return {
        "error": "404 - Paciente no encontrado"
    }



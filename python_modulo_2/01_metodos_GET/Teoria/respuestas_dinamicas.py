from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/hora-actual")
def obtener_hora():
    ahora = datetime.now()
    return {
        "fecha": ahora.strftime("%Y-%m-%d"),
        "hora": ahora.strftime("%H:%M:%S"),
        "dia_semana": ahora.strftime("%A"),
        "mes": ahora.strftime("%B"),
        "timestamp": ahora.timestamp()
    }

# uvicorn 01_metodos_GET.05_respuestas_dinamicas:app --reload
# Luego pedir que me copien lo que se añadió en el return
# hay que colocar en la terminal: uvicorn 01_metodos_GET.respuestas_dinamicas:app --reload
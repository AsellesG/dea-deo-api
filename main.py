from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Literal
import random

app = FastAPI()

class PerfilUsuario(BaseModel):
    edad: int
    genero: str
    ocasion: str
    presupuesto: float
    gustos: List[str]

class SolicitudRecomendacion(BaseModel):
    ia: Literal["DEA", "DEO"]
    perfil_usuario: PerfilUsuario

@app.post("/recomendar")
async def recomendar(solicitud: SolicitudRecomendacion):
    ia = solicitud.ia
    perfil = solicitud.perfil_usuario

    # Simulamos una lista de productos base
    productos = [
        {
            "titulo": "Cámara Digital 4K",
            "precio": 49.99,
            "url": "https://regalidea.es/products/camara-digital-4k"
        },
        {
            "titulo": "Reloj Inteligente Deportivo",
            "precio": 39.99,
            "url": "https://regalidea.es/products/reloj-inteligente"
        },
        {
            "titulo": "Mapa Rascable del Mundo",
            "precio": 19.99,
            "url": "https://regalidea.es/products/mapa-rascable"
        }
    ]

    producto = random.choice(productos)

    if ia == "DEA":
        descripcion = f"🎁 {producto['titulo']}: El detalle perfecto para un momento inolvidable. Porque cada regalo cuenta una historia."
        mensaje_final = "✨ Recuerda, el mejor regalo es el que emociona desde el primer instante. ¿Quieres otra idea?"
    else:
        descripcion = f"🔍 {producto['titulo']}: Alta funcionalidad por su precio. Ideal para un perfil como el que has descrito."
        mensaje_final = "✅ Recomendación basada en coincidencia lógica con tus criterios. ¿Quieres ver otra opción?"

    return {
        "ia": ia,
        "recomendaciones": [
            {
                "titulo": producto["titulo"],
                "descripcion": descripcion,
                "precio": producto["precio"],
                "url": producto["url"]
            }
        ],
        "mensaje_final": mensaje_final
    }

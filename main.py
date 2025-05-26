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

    producto = random.

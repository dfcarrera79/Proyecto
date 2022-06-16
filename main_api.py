from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from PicoYPlacaService import PicoYPlacaService

app = FastAPI()

origins = [    
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/be_on_road/{plate}/{date}/{time}")
def be_on_road(plate, date, time):
    service = PicoYPlacaService
    message = service.be_on_road(plate, date, time)
    return {"message": message}
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATOS_PATH = os.path.join(BASE_DIR, 'Datos_Estudiante.json')
HORARIOS_PATH = os.path.join(BASE_DIR, 'Horarios_Estudiante.json')

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de Estudiante. Endpoints disponibles: /datos_estudiante y /horarios_estudiante"}

@app.get("/datos_estudiante")
def get_datos_estudiante():
    try:
        with open(DATOS_PATH, encoding='utf-8') as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/horarios_estudiante")
def get_horarios_estudiante():
    try:
        with open(HORARIOS_PATH, encoding='utf-8') as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
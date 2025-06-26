# API Estudiante

Esta API expone los datos y horarios del estudiante a partir de archivos JSON usando FastAPI.

## Endpoints

- `/datos_estudiante`: Devuelve los datos del estudiante desde `Datos_Estudiante.json`.
- `/horarios_estudiante`: Devuelve los horarios del estudiante desde `Horarios_Estudiante.json`.

## Despliegue en Render

1. Sube este repositorio a GitHub.
2. Ve a [Render.com](https://render.com/) y crea un nuevo servicio Web.
3. Conecta tu repositorio y selecciona la carpeta `api_estudiante` como raíz.
4. Render detectará el archivo `render.yaml` y configurará el despliegue automáticamente.
5. Una vez desplegado, accede a los endpoints usando la URL proporcionada por Render.

## Desarrollo local

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Luego accede a:
- [http://localhost:8000/datos_estudiante](http://localhost:8000/datos_estudiante)
- [http://localhost:8000/horarios_estudiante](http://localhost:8000/horarios_estudiante) 
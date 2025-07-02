from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATOS_PATH = os.path.join(BASE_DIR, 'Datos_Estudiante.json')
HORARIOS_PATH = os.path.join(BASE_DIR, 'Horarios_Estudiante.json')

@app.route("/")
def root():
    return jsonify({
        "mensaje": "Bienvenido a la API de Estudiante. Endpoints disponibles: /datos_estudiante y /horarios_estudiante"
    })

@app.route("/datos_estudiante")
def get_datos_estudiante():
    try:
        with open(DATOS_PATH, encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/horarios_estudiante")
def get_horarios_estudiante():
    try:
        with open(HORARIOS_PATH, encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
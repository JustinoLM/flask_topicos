# app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/saludo', methods=['GET'])
def saludo():
    # En un caso real, aquí conectarías con MySQL y obtendrías datos
    return jsonify({"mensaje": "¡Hola desde mi API en final", "version": "6.0"})

if __name__ == '__main__':
    # Escucha en todas las interfaces para Docker
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify

app = Flask(__name__)

Usuarios = [
    {"id": 1, "nome": "Mark Ribeiro dos Santos"},
    {"id": 2, "nome": "Charles Leclerc"},
    {"id": 3, "nome": "Mr. Sixseven"},
    {"id": 4, "nome": "Raphael Veiga"},
    {"id": 5, "nome": "Abel Ferreira"},
]

@app.route("/usuarios", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Usuários - Acesse /usuarios"})

@app.route("/", methods=["GET"])
def listar_usuarios():
    return jsonify(__name__)

if __name__ == "_main_":
    app.run(port=5001)

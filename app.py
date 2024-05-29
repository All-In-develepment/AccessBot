from flask import Flask, request
from db.mongo import CreateConnection

app = Flask(__name__)

@app.route('/inserir', methods=['POST'])
def inserir():
    collection = CreateConnection()
    # Assume que o corpo da requisição é um JSON
    dados = request.json
    # Insere os dados no MongoDB
    resultado = collection.insert_one(dados)
    # Retorna uma resposta
    return {'status': 'sucesso', 'id_inserido': str(resultado.inserted_id)}

if __name__ == '__main__':
    app.run(debug=True)

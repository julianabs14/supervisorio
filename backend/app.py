from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def inicio():
    return jsonify({'mensagem': 'API Technosensor funcionando'})

@app.route('/status')
def status():
    dados = {
        'status': 'EM OPEREÇÃO',
        'pecas_inspecionadas': 9842,
        'pecas_aprovadas': 9102,
        'pecas_rejeitadas': 740,
        'taxa_rejeicao': 7.53
    }
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
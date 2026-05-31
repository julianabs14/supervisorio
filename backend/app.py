from flask import Flask, jsonify
from flask_cors import CORS
import openpyxl

app = Flask(__name__)
CORS(app)

@app.route('/')
def inicio():
    return jsonify({'mensagem': 'API Technosensor funcionando'})

@app.route('/status')
def status():

    base_de_dados = openpyxl.load_workbook('dados.xlsx')

    aba = base_de_dados.active

    dados = {
        'status': aba['A2'].value,
        'pecas_inspecionadas': aba['B2'].value,
        'pecas_aprovadas': aba['C2'].value,
        'pecas_rejeitadas': aba['D2'].value,
        'taxa_rejeicao': aba['E2'].value
    }
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
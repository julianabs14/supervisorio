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
    'status': aba.cell(row=2, column=1).value,
    'pecas_inspecionadas': aba.cell(row=2, column=2).value,
    'pecas_aprovadas': aba.cell(row=2, column=3).value,
    'pecas_rejeitadas': aba.cell(row=2, column=4).value,
    'taxa_rejeiao': aba.cell(row=2, column=5).value
}
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
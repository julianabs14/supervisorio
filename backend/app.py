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

    def converter(valor):
        if valor is None:
            return ''
        return str(valor)

    dados = {
    'status': aba.cell(row=2, column=1).value,
    'pecas_inspecionadas': aba.cell(row=2, column=2).value,
    'pecas_aprovadas': aba.cell(row=2, column=3).value,
    'pecas_rejeitadas': aba.cell(row=2, column=4).value,
    'taxa_rejeiao': aba.cell(row=2, column=5).value,
    'inicio_parada': converter(aba.cell(row=2, column=6).value),
    'tempo_parado': converter(aba.cell(row=2, column=7).value),
    'media_paradas': converter(aba.cell(row=2, column=8).value),
    'total_paradas': converter(aba.cell(row=2, column=9).value),
    'status_garrafa': aba.cell(row=2, column=10).value,
    'camera': aba.cell(row=2, column=11).value,
    'confianca': aba.cell(row=2, column=12).value,
    'trinca': aba.cell(row=2, column=13).value,
    'mancha': aba.cell(row=2, column=14).value,
    'soda': aba.cell(row=2, column=15).value,
    'sujeira': aba.cell(row=2, column=16).value,
    'risco': aba.cell(row=2, column=17).value,
    'outros': aba.cell(row=2, column=18).value,
    'marca': aba.cell(row=2, column=19).value,
    'sku': aba.cell(row=2, column=20).value,
    'lote': aba.cell(row=2, column=21).value,
    'envase': converter(aba.cell(row=2, column=22).value),
    'linha': aba.cell(row=2, column=23).value,
    'velocidade': aba.cell(row=2, column=24).value,
    'eficiencia': aba.cell(row=2, column=25).value,
    'disponibilidade': aba.cell(row=2, column=26).value,
    'qualidade': aba.cell(row=2, column=27).value,
    'oee': aba.cell(row=2, column=28).value,
    'mtbf': converter(aba.cell(row=2, column=28).value),
    'mttr': converter(aba.cell(row=2, column=29).value)

}
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
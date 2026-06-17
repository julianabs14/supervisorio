from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import openpyxl
from datetime import time, date, datetime
import re

app = Flask(__name__)
CORS(app)

def extrairNumero(valor):
    if not valor:
        return 0
    return int(str(valor).split()[0])

@app.route('/app')
def inicio():
    return send_from_directory('../frontend', 'supervisorio.html')

@app.route('/status')
def status():

    base_de_dados = openpyxl.load_workbook('dados.xlsx')

    aba = base_de_dados['Planilha1']

    def converter(valor):
        if valor is None:
            return ''
        if isinstance(valor, (time, date, datetime)):
            return valor.strftime('%H:%M:%S')
        return str(valor)

    falhas_brutas = {
        'Trinca': aba.cell(row=2, column=13).value or '',
        'Mancha': aba.cell(row=2, column=14).value or '',
        'Soda cáustica': aba.cell(row=2, column=15).value or '',
        'Sujeira': aba.cell(row=2, column=16).value or '',
        'Risco': aba.cell(row=2, column=17).value or '',
        'Outro': aba.cell(row=2, column=18).value or '',
    }

    falhas_ordenadas = sorted(falhas_brutas.items(), key=lambda x: extrairNumero(x[1]), reverse=True)

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
        'confianca': converter(aba.cell(row=2, column=12).value),
        'marca': aba.cell(row=2, column=19).value,
        'sku': aba.cell(row=2, column=20).value,
        'lote': aba.cell(row=2, column=21).value,
        'envase': converter(aba.cell(row=2, column=22).value),
        'linha': aba.cell(row=2, column=23).value,
        'velocidade': converter(aba.cell(row=2, column=24).value),
        'eficiencia': aba.cell(row=2, column=25).value,
        'disponibilidade': aba.cell(row=2, column=26).value,
        'opi': aba.cell(row=2, column=27).value,
        'oee': converter(aba.cell(row=2, column=28).value) + '%',
        'mtbf': converter(aba.cell(row=2, column=29).value),
        'mttr': converter(aba.cell(row=2, column=30).value),
        'total_cameras': aba.cell(row=2, column=34).value,
        'total_triggers': aba.cell(row=2, column=35).value,
        'temperatura': converter(aba.cell(row=2, column=36).value),
        'iluminacao': aba.cell(row=2, column=37).value,
        'comunicacao': aba.cell(row=2, column=38).value,
        'alertas': [
            {
                'hora': converter(aba.cell(row=i, column=31).value),
                'evento': converter(aba.cell(row=i, column=32).value),
                'causa': converter(aba.cell(row=i, column=33).value)
            }
            for i in range(2, 7)
        ],
        'falhas_brutas': falhas_brutas,
        'falhas_ordenadas': falhas_ordenadas,
        'top_falhas': [
            {'nome': nome, 'valor': valor}
            for nome, valor in falhas_ordenadas
        ]
    }

    return jsonify(dados)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    if request.method == 'OPTIONS':
        return '', 204

    dados = request.get_json(force=True)
    print(dados)
    print(type(dados))

    if isinstance(dados, list):
        dados = dados[0]

    nome = str(dados['nome'])
    usuario = str(dados['usuario'])
    senha = str(dados['senha'])

    baseDados = openpyxl.load_workbook('dados.xlsx')
    aba_usuarios = baseDados['usuarios']

    for linha in aba_usuarios.iter_rows(min_row=2, values_only=True):
        if linha[1] == usuario:
            return jsonify({'sucesso': False, 'mensagem': 'Usuário já existe'})
        
    aba_usuarios.append([nome, usuario, senha])
    baseDados.save('dados.xlsx')

    return jsonify({'sucesso': True, 'mensagem': 'Cadastro realizado'})

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'OPTIONS':
        return '', 204

    dados = request.get_json(force=True)
    print(dados)

    usuario_digitado = str(dados['usuario'])
    senha_digitada = str(dados['senha'])

    basedados = openpyxl.load_workbook('dados.xlsx')
    aba_usuarios = basedados['usuarios']

    for linha in aba_usuarios.iter_rows(min_row=2, values_only=True):
        nome, usuario, senha = linha
        if usuario == usuario_digitado and senha == senha_digitada == senha_digitada:
            return jsonify({'sucesso': True, 'nome': nome})
    
    return jsonify({'Sucesso':False, 'mensagem':'Usuário ou senha incorretos'})

if __name__ == '__main__':
    app.run(debug=True)
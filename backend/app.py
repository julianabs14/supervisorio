import sqlite3
from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import datetime
import re
import bcrypt
import jwt
from dotenv import load_dotenv
import os
from functools import wraps

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def init_db():
    conexao = sqlite3.connect('tecnosensor.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXIST usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()

def criar_hash_senha(senha):
    senha_bytes = senha.encode('utf-8')
    hash_gerado = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
    return hash_gerado('utf-8')

def verificar_senha(senha_digitada, hash_salvo):
    senha_bytes = senha_digitada.encode('utf-8')
    hash_bytes = hash_salvo.encode('utf-8')
    return bcrypt.checkpw(senha_bytes, hash_bytes)

def token_obrigatorio(funcao):
    @wraps(funcao)

    def decorador(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'mensagem': 'Token não fornecido!'}), 401
        
        try:
            jwt.decode(token, SECRET_KEY, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            return jsonify({'mensagem': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'mensagem': 'Token inválida'}), 401
        
    return decorador

app = Flask(__name__)
CORS(app)

@app.route('/app')
def inicio():
    return send_from_directory('../frontend', 'supervisorio.html')

@app.route('/status')
@token_obrigatorio
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

    nome = str(dados['nome'])
    usuario = str(dados['usuario'])
    senha = str(dados['senha'])

    if not nome or not usuario or not senha:
        return jsonify({'sucesso': False, 'mensagem': 'Todos os campos são obrigatórios! '}), 400
    
    if len(senha) < 6:
        return jsonify({'sucesso': False, 'mensagem': 'A senha deve ter ao menos 6 caracteres! '}), 400
    
    senha_hash = criar_hash_senha(senha)

    try:
        conexao = sqlite3.connect('technosesnor.db')
        cursor = conexao.cursor()

        cursor.execute('''
            INSERT INTO (nome, usuario, senha),
            VALUES(?, ?, ?)

        ''', (nome, usuario, senha_hash))

        conexao.commit()
        conexao.close()

        return jsonify({'sucesso': True, 'mensagem': 'Cadastro realizado com sucesso! '})
    
    except sqlite3.IntegrityError:
        return jsonify({'sucesso': False, 'mensagem': 'Usuário já existe!'}), 409

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'OPTIONS':
        return '', 204

    dados = request.get_json(force=True)

    usuario = usuario.get('usuario')
    senha =senha.get('senha')

    if not usuario or not senha:
        return jsonify({'sucesso': False, 'mensagem': 'Usuário e senha são obrigatórios! '}), 400
    
    conexao = sqlite3.connect('technosensor.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT nome, senha FROM usuarios WHERE usuario = ?', (usuario,))

    resultado = cursor.fetchone()
    conexao.close()

    if resultado is None:
        return jsonify({'sucesso': False, 'mensagem': 'Usuário ou senha incorretos'}), 401
    
    nome_encontrado, senha_hash_salva = resultado

    if not verificar_senha(senha, senha_hash_salva):
        return jsonify({'sucesso': False, 'mensagem': 'Usuário ou senha incorretos'}), 401
    
    payload = {
        'usuario': usuario,
        'nome': nome_encontrado,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
    return jsonify({'sucesso': True, 'nome': nome_encontrado, 'token': token })

if __name__ == '__main__':
    app.run(debug=True)
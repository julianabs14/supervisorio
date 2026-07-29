# TecnoSensor — Supervisório de Manutenção Preditiva

> 🇧🇷 Português | 🇺🇸 [English below](#english)

---

## 🇧🇷 Português

Sistema web fullstack para monitoramento de máquinas industriais em tempo real, desenvolvido como projeto de conclusão de curso (TCC) no SENAI.

### Demonstração
[technosensor.onrender.com](https://technosensor.onrender.com)

### Funcionalidades
- Login e cadastro de usuários com autenticação segura
- Dashboard com dados em tempo real organizados por seções
- Gráfico comparativo MTBF vs MTTR
- Geração de relatório em Excel com os principais problemas
- Proteção de rotas via JWT
- Rate limiting contra ataques de força bruta

### Tecnologias
| Camada | Tecnologia |
|---|---|
| Front-end | HTML, CSS, JavaScript (SPA) |
| Back-end | Python + Flask |
| Banco de dados | SQLite |
| Autenticação | JWT + bcrypt |
| Gráficos | Chart.js |
| Relatórios | openpyxl |
| Deploy | Render |

### Segurança
- Senhas criptografadas com bcrypt
- Autenticação via token JWT com expiração de 8 horas
- Rate limiting nas rotas de login e cadastro
- Proteção contra SQL Injection via prepared statements
- Variáveis sensíveis via `.env`

### Como rodar localmente
```bash
# Clone o repositório
git clone https://github.com/julianabs14/supervisorio.git

# Entre na pasta do backend
cd supervisorio/backend

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
# Crie um arquivo .env com:
# SECRET_KEY=sua_chave_secreta_aqui

# Inicie o servidor
python app.py

# Acesse no navegador
# http://127.0.0.1:5000
```

### Desenvolvedora
**Juliana Bezerra** — Aprendiz em Eletromecânica | Processos @ Heineken Brasil | Engenharia de Software

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Juliana_Bezerra-blue)](https://www.linkedin.com/in/juliana-bezerra-03b8562b4/)
[![GitHub](https://img.shields.io/badge/GitHub-julianabs14-black)](https://github.com/julianabs14)

---

## 🇺🇸 English <a name="english"></a>

Fullstack web system for real-time industrial machine monitoring, developed as a final course project (TCC) at SENAI.

### Live Demo
[technosensor.onrender.com](https://technosensor.onrender.com)

### Features
- User login and registration with secure authentication
- Dashboard with real-time data organized by sections
- MTBF vs MTTR comparison chart
- Excel report generation with top issues
- Route protection via JWT
- Rate limiting against brute force attacks

### Tech Stack
| Layer | Technology |
|---|---|
| Front-end | HTML, CSS, JavaScript (SPA) |
| Back-end | Python + Flask |
| Database | SQLite |
| Authentication | JWT + bcrypt |
| Charts | Chart.js |
| Reports | openpyxl |
| Deploy | Render |

### Security
- Passwords hashed with bcrypt
- JWT token authentication with 8-hour expiration
- Rate limiting on login and registration routes
- SQL Injection protection via prepared statements
- Sensitive variables via `.env`

### How to run locally
```bash
# Clone the repository
git clone https://github.com/julianabs14/supervisorio.git

# Go to backend folder
cd supervisorio/backend

# Install dependencies
pip install -r requirements.txt

# Set environment variables
# Create a .env file with:
# SECRET_KEY=your_secret_key_here

# Start the server
python app.py

# Open in browser
# http://127.0.0.1:5000
```

###  Developer
**Juliana Bezerra** — Electromechanics Apprentice | Brewery @ Heineken Brasil | Software Engineering Student

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Juliana_Bezerra-blue)](https://www.linkedin.com/in/juliana-bezerra-03b8562b4/)
[![GitHub](https://img.shields.io/badge/GitHub-julianabs14-black)](https://github.com/julianabs14)
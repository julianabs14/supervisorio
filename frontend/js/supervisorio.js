//navegação 
const usuarioLogado = localStorage.getItem('usuarioLogado');

if (!usuarioLogado) {
    window.location.href = 'index.html';

};

document.getElementById('nome-usuario').textContent = usuarioLogado

const botoes = document.querySelectorAll('.btn-nav, .btn-nav-ativo');

botoes.forEach(function(botao){
    botao.addEventListener('click', function() {
        
        document.querySelectorAll('.secao').forEach(function(secao) {
            secao.classList.remove('ativa');
        });

        botoes.forEach(function(b){
            b.className = 'btn-nav';
        });

        const alvo = this.dataset.secao;

        document.getElementById(alvo).classList.add('ativa');

        this.className = 'btn-nav-ativo';

    });
});

document.getElementById('btn-logout').addEventListener('click', function() {
    localStorage.removeItem('usuarioLogado')
    window.location.href = 'index.html'
});

fetch('http://127.0.0.1:5000/status')
    .then(function(resposta) {
        return resposta.json()
    })
    .then(function(dados) {
        document.querySelector('.status-texto').textContent = dados.status
        document.getElementById('pecas-inspecionadas').textContent = dados.pecas_inspecionadas + ' unidades'
        document.getElementById('pecas-aprovadas').textContent = dados.pecas_aprovadas + ' unidades'
        document.getElementById('pecas-rejeitadas').textContent = dados.pecas_rejeitadas + ' unidades'
        document.getElementById('taxa-rejeicao').textContent = dados.taxa_rejeiao + '%'
        document.getElementById('inicio-parada').textContent = dados.inicio_parada
        document.getElementById('tempo-parado').textContent = dados.tempo_parado
        document.getElementById('media-paradas').textContent = dados.media_paradas
        document.getElementById('total-paradas').textContent = dados.total_paradas
    });
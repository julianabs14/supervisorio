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
        document.getElementById('status-garrafa').textContent = dados.status_garrafa
        document.getElementById('camera').textContent = dados.camera
        document.getElementById('confianca').textContent = dados.confianca
        document.getElementById('trinca').textContent = dados.trinca
        document.getElementById('mancha').textContent = dados.mancha
        document.getElementById('soda').textContent = dados.soda
        document.getElementById('sujeira').textContent = dados.sujeira
        document.getElementById('risco').textContent = dados.risco
        document.getElementById('outros').textContent = dados.outros
        document.getElementById('marca').textContent = dados.marca
        document.getElementById('sku').textContent = dados.sku
        document.getElementById('lote').textContent = dados.lote
        document.getElementById('envase').textContent = dados.envase
        document.getElementById('linha').textContent = dados.linha
        document.getElementById('velocidade').textContent = dados.velocidade + 'un/h'
        document.getElementById('eficiencia').textContent = dados.eficiencia + '%'
        document.getElementById('disponibilidade').textContent = dados.disponibilidade + '%'
        document.getElementById('qualidade').textContent = dados.qualidade + '%'
        document.getElementById('oee').textContent = dados.oee
        document.getElementById('mtbf').textContent = dados.mtbf
        document.getElementById('mttr').textContent = dados.mttr

    });
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
    localStorage.clear()
    window.location.href = 'index.html'
});

const token = localStorage.getItem('token')

fetch('http://127.0.0.1:5000/status', {
    method: 'GET',
    headers:{
        'Authorization': token,
        'Content-Type': 'application/json'
    }    
})
    .then(function(resposta){
        if (resposta.status === 401) {
            localStorage.clear()
            window.location.href = 'index.html'
        }
    return resposta.json()

    })
    .then(function(dados) {
        document.querySelector('.status-texto').textContent = dados.status;
        document.getElementById('pecas-inspecionadas').textContent = dados.pecas_inspecionadas  + ' unidades';
        document.getElementById('pecas-aprovadas').textContent = dados.pecas_aprovadas + ' unidades';
        document.getElementById('pecas-rejeitadas').textContent = dados.pecas_rejeitadas + ' unidades';
        document.getElementById('taxa-rejeicao').textContent = dados.taxa_rejeicao+ '%';
        document.getElementById('inicio-parada').textContent = dados.inicio_parada + ' Hrs';
        document.getElementById('tempo-parado').textContent = dados.tempo_parado + ' Hrs';
        document.getElementById('media-paradas').textContent = dados.media_paradas + ' Hrs';
        document.getElementById('total-paradas').textContent = dados.total_paradas;
        document.getElementById('status-garrafa').textContent = dados.status_garrafa;
        document.getElementById('camera').textContent = dados.camera;
        document.getElementById('confianca').textContent = dados.confianca;

        const cardFalhas = document.getElementById('card-top-falhas');
        cardFalhas.querySelectorAll('.linha-dado').forEach(el => el.remove());

        const cores = ['vermelho', 'amarelo', 'amarelo', '', '', ''];

        dados.top_falhas.forEach(function(falha, index) {
            const linha = document.createElement('div');
            linha.className = 'linha-dado';
            linha.innerHTML = `
                <span>${index + 1}. ${falha.nome}</span>
                <span class="valor ${cores[index] || ''}">${falha.valor}</span>     
            `;
        cardFalhas.appendChild(linha);
        });

        document.getElementById('marca').textContent = dados.marca;
        document.getElementById('sku').textContent = dados.sku;
        document.getElementById('lote').textContent = dados.lote;
        document.getElementById('envase').textContent = dados.envase;
        document.getElementById('linha').textContent = dados.linha;
        document.getElementById('velocidade').textContent = dados.velocidade + ' Un/H';
        document.getElementById('eficiencia').textContent = dados.eficiencia + '%';
        document.getElementById('disponibilidade').textContent = dados.disponibilidade + '%';
        document.getElementById('opi').textContent = dados.opi + '%';
        document.getElementById('oee').textContent = dados.oee + '%';
        document.getElementById('mtbf').textContent = dados.mtbf + ' Hrs';
        document.getElementById('mttr').textContent = dados.mttr + ' Hrs';
        document.getElementById('total-cameras').textContent = dados.total_cameras;
        document.getElementById('total-triggers').textContent = dados.total_triggers;
        document.getElementById('temperatura').textContent = dados.temperatura;
        document.getElementById('iluminacao').textContent = dados.iluminacao;
        document.getElementById('comunicacao').textContent = dados.comunicacao;

        const linhas = document.querySelectorAll('#card-alertas .linha-dado');

        dados.alertas.forEach(function(alerta, index) {
            if (!linhas[index]) return;
            linhas[index].querySelector('.hora').textContent = alerta.hora;
            linhas[index].querySelector('.evento').textContent = alerta.evento;
            linhas[index].querySelector('.causa').textContent = alerta.causa;
        });

    });
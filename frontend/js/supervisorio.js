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
})
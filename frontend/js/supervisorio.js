//navegação 
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
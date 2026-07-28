const formCadastro = document.getElementById('form-cadastro');

formCadastro.addEventListener('submit', function(evento) {
    evento.preventDefault();

    const nome = document.getElementById('nome').value;
    const usuario = document.getElementById('novo-usuario').value;
    const senha = document.getElementById('nova-senha').value
    const confirma = document.getElementById('confirmar-senha').value

    if (senha < 6) {
        alert('A senha deve ter ao menos 6 caracteres')
        return
    }
    
    if (senha !== confirma) {
        alert('As senhas não coincidem!');
        return
    }

    if (!nome | !usuario | !senha) {
        alert('Preencha todos os campos!');
        return
    }

    fetch('/cadastro', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({nome: nome, usuario: usuario,senha: senha})
    })
    .then(function(resposta) {
        return resposta.json()
    })
    .then(function(dados){
        if (dados.sucesso){
            alert('Conta criada com sucesso! Faça login.')
            window.location.href = 'index.html'
        } else {
            alert(dados.mensagem)
        }
    });

});
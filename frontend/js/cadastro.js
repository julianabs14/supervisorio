const formCadastro = document.getElementById('form-cadastro');

formCadastro.addEventListener('submit', function(evento) {
    evento.preventDefault();

    const nome = document.getElementById('nome').value;
    const usuario = document.getElementById('novo-usuario').value;
    const senha = document.getElementById('nova-senha').value
    const confirma = document.getElementById('confirmar-senha').value

    if (senha !== confirma) {
        alert('As senhas não coincidem!');
        return
    }

    if (!nome | !usuario | !senha) {
        alert('Preencha todos os campos!');
        return
    }

    alert('Conta criada com sucesso! Faça o login.');
    window.location.href = 'index.html';
});
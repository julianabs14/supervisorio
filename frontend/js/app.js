//login tempóraio, array de objetos

const usuarios = [
    { usuario: 'admin', senha: '1234', nome: 'Administrador'},
    { usuario: 'tecnico', senha: 'senai', nome: 'Técnico I'}
];

const formLogin = document.getElementById('form-login');

formLogin.addEventListener('submit', function(evento) {
    evento.preventDefault();

    const digitouUsuario = document.getElementById('usuario').value; 
    const digitouSenha = document.getElementById('senha').value;

    const encontrado = usuarios.find(function(item) {
        return item.usuario === digitouUsuario && item.senha === digitouSenha;
    });

    if (encontrado) {
        alert('Bem-vindo, ' + encontrado.nome);
        localStorage.setItem('usuarioLogado', encontrado.nome)
        window.location.href = 'supervisorio.html'
    } else {
        alert('Usuário ou senha incorretos');
    }
});

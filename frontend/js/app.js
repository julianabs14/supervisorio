//login tempóraio, array de objetos

const usuarios = [];

const formLogin = document.getElementById('form-login');

formLogin.addEventListener('submit', function(evento) {
    evento.preventDefault();

    const digitouUsuario = document.getElementById('usuario').value; 
    const digitouSenha = document.getElementById('senha').value;

   fetch('http://127.0.0.1:5000/login', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({usuario: digitouUsuario, senha: digitouSenha})
   })
   .then(function(resposta){
        return resposta.json()
   })
   .then(function(dados){
    if (dados.sucesso) {
        localStorage.setItem('usuarioLogado', dados.nome)
        window.location.href ='supervisorio.html'
    }  else  {
        alert(dados.mensagem)
    }
   })
});

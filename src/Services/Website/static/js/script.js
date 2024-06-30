document.addEventListener('DOMContentLoaded', function() {
    // Validação do formulário de registro
    document.getElementById('registerForm').addEventListener('submit', function(event) {
        event.preventDefault();
        let username = document.getElementById('username').value;
        let email = document.getElementById('email').value;
        let password = document.getElementById('password').value;

        if(username && email && password) {
            alert('Registro bem-sucedido!');
            // Aqui você pode adicionar a lógica para enviar os dados ao servidor
        } else {
            alert('Preencha todos os campos.');
        }
    });

    // Validação do formulário de login
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault();
        let username = document.getElementById('usernameLogin').value;
        let password = document.getElementById('passwordLogin').value;

        if(username && password) {
            alert('Login bem-sucedido!');
            // Aqui você pode adicionar a lógica para enviar os dados ao servidor
        } else {
            alert('Preencha todos os campos.');
        }
    });

    // Função de exemplo para exibir dados climáticos (substitua com dados reais)
    function displayClimateData() {
        const dataDisplay = document.getElementById('data-display');
        const data = [
            { temperature: '25°C', humidity: '60%', windSpeed: '10 km/h', pressure: '1013 hPa', weather: 'Clear', location: 'São Paulo' },
            // Adicione mais dados conforme necessário
        ];

        data.forEach(item => {
            let dataDiv = document.createElement('div');
            dataDiv.textContent = `Temperatura: ${item.temperature}, Umidade: ${item.humidity}, Velocidade do Vento: ${item.windSpeed}, Pressão: ${item.pressure}, Tempo: ${item.weather}, Localização: ${item.location}`;
            dataDisplay.appendChild(dataDiv);
        });
    }

    // Função de exemplo para exibir lista de usuários (substitua com dados reais)
    function displayUserList() {
        const userList = document.getElementById('user-list');
        const users = [
            { username: 'user1', email: 'user1@example.com' },
            // Adicione mais usuários conforme necessário
        ];

        users.forEach(user => {
            let userDiv = document.createElement('div');
            userDiv.textContent = `Usuário: ${user.username}, Email: ${user.email}`;
            userList.appendChild(userDiv);
        });
    }

    // Chamando as funções de exibição (isso seria feito após carregar dados reais)
    displayClimateData();
    displayUserList();
});

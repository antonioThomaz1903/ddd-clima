from flask_mail import Mail, Message
from src.app import app, settings
import requests
from src.app import session_app
from src.Entities import Usuario
from src.Services.ColetarDados import getDadosClimaticos
def enviar_newsletter():
	usuarios = session_app.query(Usuario).all()
	destinatarios = []
	for usuario in usuarios:
		destinatarios.append(usuario.email)
	dados = getDadosClimaticos()
	conteudo = ""
	for dado in dados:
		conteudo += dado.__str__() + "\n"
	return requests.post(
		"https://api.mailgun.net/v3/sandboxf22af85344f04dac96b8addc6100a9df.mailgun.org/messages",
		auth=("api", settings.EMAIL_API_KEY),
		data={"from": "mailgun@sandboxf22af85344f04dac96b8addc6100a9df.mailgun.org",
			"to": destinatarios,
			"subject": "Dados Coletados",
			"text": conteudo})

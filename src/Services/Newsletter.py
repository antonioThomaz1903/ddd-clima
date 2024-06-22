from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações de email (usando Gmail como exemplo)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'antoniothomazoliveirareis@gmail.com'
app.config['MAIL_PASSWORD'] = 'eoq'

mail = Mail(app)


@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'error': 'Email is required'}), 400

    # Simula a adição do email a um banco de dados ou lista
    print(f'Novo inscrito: {email}')

    # Envia email de boas-vindas
    msg = Message('Bem-vindo à Newsletter!',
                  sender='seu-email@gmail.com',
                  recipients=[email])
    msg.body = 'Obrigado por se inscrever em nossa newsletter!'

    try:
        mail.send(msg)
        return jsonify({'message': 'Inscrição realizada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000)

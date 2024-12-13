import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Olá, Tudo bem?!</p>
    <hr>
    <p>Essa é uma mensagem de preenchimento para o envio do email.</p>
    """

    msg = email.message.Message()

    msg['Subject'] = 'Esses é o ASSUNTO do meu email: Email Teste'
    msg['From'] = 'Emissor'
    msg['To'] = 'Recepitor'

    # Senha de app do Gmail
    password = 'SenhadeEmail'

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)

    try:
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email Enviado!')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

enviar_email()
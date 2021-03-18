from flask_mail import Message
from flask import current_app

from agro.ext.email import mail

def enviar_email(para, descricao, template):
    msg = Message(
        descricao,
        recipients=[para],
        html=template,
        sender=current_app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)

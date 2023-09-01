from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config


def send_email(
    recipients: list[str],
    mail_body: str,
    mail_subject: str,
    attachment: str = None,
):
    SERVER = config.SMTP_SERVER
    PASSWORD = config.TOKEN_API
    USER = config.USER

    msg = MIMEMultipart('alternative')
    msg['Subject'] = mail_subject
    msg['From'] = f'<Lection 13 user {USER}>'
    msg['To'] = ', '.join(recipients)
    msg['Reply-To'] = USER
    msg['Return-Path'] = USER
    msg['X-Mailer'] = 'decorator'

    text_to_send =








def check_email():
    pass

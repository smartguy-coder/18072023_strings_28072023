from email.mime.multipart import MIMEMultipart

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





def check_email():
    pass

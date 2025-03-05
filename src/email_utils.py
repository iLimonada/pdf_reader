import smtplib
from email.message import EmailMessage
import os
from config import SMTP_SERVER, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD

def enviar_gmail(recipient, subject, body, attachment):
    """Envio de gmail com anexo"""
    msg = EmailMessage()
    msg = EmailMessage()
    msg["From"] = EMAIL_SENDER
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with open(attachment, "rb") as file:
            msg.add_attachment(file.read(), maintype="application", subtype="xlsx", filename=os.path.basename(attachment))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"E-mail enviado com sucesso para {recipient}!")

    except Exception as ex:
        print(f"Erro ao enviar email: {ex}")
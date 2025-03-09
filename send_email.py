import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(message):
    host = "smtp.gmail.com"
    sender_email = "adil.study.ali7047@gmail.com"
    port = 465
    sender_password = os.getenv("PASSWORD")

    receiver_email = "adil.study.ali7047@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "News Headlines"
    message = message + "\n\nBest Regards,\nAdil Ali"
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    ssl_key = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=ssl_key) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

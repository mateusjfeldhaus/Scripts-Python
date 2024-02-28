import smtplib


def send_mail():
    email = ""
    password = ""

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    # server.starttls()
    server.ehlo()
    server.login(email, password)

    subject = "Alerta Python"
    body = "Compre agora, o link é "

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(email, msg)

# sender_email = "pythonj49@gmail.com"
# app_pass = "sylg nini xrfv xyhh"
import smtplib
from email.mime.text import MIMEText

subject = "سلام  و وقت بخیر"
body = "سلام این نامه از طرف کلاس پایتون ارسال شده است."
sender = "pythonj49@gmail.com"
recipients = ["h.qorbani7@gmail.com", "Fatmhrwhafzayy@gmail.com"]
password = "sylg nini xrfv xyhh"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)
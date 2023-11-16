import json
import smtplib
from email.mime.text import MIMEText
#-----json
def read_json(file_address):
    json_data = open(file_address)
    return json.load(json_data)

def write_json(file_address , data):
    json_object = json.dumps(data, indent = 4)
    # Writing to pizzas.json
    with open(file_address, "w") as outfile:
        outfile.write(json_object)
#-------end json

#-----email:
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")
#----end email
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Message Body email:
msg = MIMEMultipart()
message = "You received a new email from PycodeBR"

# Parameters and Title:
password = "*password of your email*"
msg['From'] = "*email to use*"
msg['To'] = "*email that arrived*"
msg['Subject'] = "Received Gmail with Python on PyCharm"

# Constructor connection and send the email:
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port = 987)

# Configure the server:
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())

# Interrupting the operations:
server.quit()
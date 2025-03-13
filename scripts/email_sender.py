import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg['From'] = "from@mail.ru"
msg['To'] = "to@mail.ru"
msg['Subject'] = "Hello world"
msg.attach(MIMEText("Message body = hello man", 'plain'))

server = smtplib.SMTP('smtp.mail.ru', 465)
server.starttls()
server.login("your@mail.ru", "password")
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

import smtplib
from email.mime.text import MIMEText
import pandas as pd

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'santoshwar.dhruv11@gmail.com'
password = 'dhruvs123'
sender = 'santoshwar.dhruv11@gmail.com'
#targets = ['chaityavwcr07@gmail.com','santoshwar.dhruv11@gmail.com']

columns_name=["Name","email","Phone"]
df=pd.read_csv("sample.csv",names=columns_name)
names_list=df.Name.to_list()
email_list=df.email.to_list()


server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
for i in range(len(email_list)):
    email_temp=email_list[i:i+1]
    name_temp=names_list[i]
    msg = MIMEText(f'Hi {name_temp} this is just testing mail \nPlease ignore\nThank you bsdke')
    msg['Subject'] = 'Sab moh maya corporation ltd'
    msg['From'] = sender
    msg['To'] = ', '.join(email_temp)

    server.sendmail(sender, email_temp, msg.as_string())


server.quit()





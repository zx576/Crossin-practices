import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

mail_host = 'smtp.163.com'
mail_user = '15922860402'
mail_pass = '775466743zx'
sender = '15922860402@163.com'
receivers = ['782744680@qq.com']


message = MIMEMultipart('alternative')
message['From'] = sender
message['To'] = receivers[0]
message['Subject'] = 'title'
with open('abc.html','r') as f:
    content = f.read()
part1 = MIMEText(content,'html','utf-8')
with open('abc.txt','r')as h:
    content2 = h.read()
part2 = MIMEText(content2,'utf-8')
message.attach(part1)
message.attach(part2)
with open('1.png','rb')as fp:
    picture = MIMEText(fp.read(),'base64','utf-8')
    picture['Content-Type'] = 'application/octet-stream'
    picture['Content-Disposition'] = 'attachment;filename="1.png"'
message.attach(picture)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    print('cc')
    smtpObj.login(mail_user,mail_pass)
    print('lg')
    smtpObj.sendmail(sender,receivers,message.as_string())
    # smtpObj.send_message(message)
    print('success')
    smtpObj.quit()
except smtplib.SMTPException as e:
    print('error',e)
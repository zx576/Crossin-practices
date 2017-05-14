import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.163.com'
mail_user = '15922860402'
mail_pass = '775466743zx'
sender = '15922860402@163.com'
receivers = ['782744680@qq.com']

with open('abc.html','r') as f:
    content = f.read()
message = MIMEText(content,'html','utf-8')
# message['From'] = Header('这是一封正经的邮件','utf-8')
message['From'] = sender
# message['To'] = Header('真的是很正式','utf-8')
message['To'] = receivers[0]

subject = 'title'
message['Subject'] = subject
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
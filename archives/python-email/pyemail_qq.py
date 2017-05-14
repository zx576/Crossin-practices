import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.qq.com'
mail_user = '782744680@qq.com'
mail_pass = 'ugqhlweebvqwbecc'

sender = '782744680@qq.com'
receivers = ['15922860402@163.com']

message = MIMEText('今天完成任务today','plain','utf-8')
# message['From'] = Header('这是一封正经的邮件','utf-8')
message['From'] = sender
# message['To'] = Header('真的是很正式','utf-8')
message['To'] = receivers[0]

subject = '闵行紫竹kaifaqu'
message['Subject'] = Header(subject,'utf-8')
try:
    smtpObj = smtplib.SMTP_SSL(mail_host)
    # smtpObj.set_debuglevel(1)
    # smtpObj.connect(mail_host)
    print('cc')
    smtpObj.login(mail_user,mail_pass)
    print('lg')
    smtpObj.sendmail(sender,receivers,message.as_string())
    # smtpObj.send_message(message)
    print('success')
    smtpObj.quit()
except smtplib.SMTPException as e:
    print('error',e)
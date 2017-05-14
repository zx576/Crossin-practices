import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.cqu.edu.cn'
mail_user = '20113839'
mail_pass = '10102078'

sender = '20113839@cqu.edu.cn'
receivers = ['782744680@qq.com']

message = MIMEText('今天完成任务','plain','utf-8')
# message['From'] = Header('这是一封正经的邮件','utf-8')
message['From'] = sender
# message['To'] = Header('真的是很正式','utf-8')
message['To'] = receivers[0]

subject = '闵行紫竹'
message['Subject'] = Header(subject,'utf-8')
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
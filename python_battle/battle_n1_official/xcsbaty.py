#  coding=gbk

import time
import urllib2
from bs4 import BeautifulSoup
import re
# import sys
# reload(sys)
# sys.setdefaultencoding('gbk')

m = time.strftime('%m',time.localtime())
day = time.strftime('%m/%d/',time.localtime())
y = time.strftime('%Y',time.localtime())
age = int(y) - 1984


time_now = time.strftime('%Y%m%d',time.localtime())
# print "today is %s"%time_now
# print "movies:",


###get douban movie list ###

url = "http://movie.douban.com/later/ziyang"
html = urllib2.urlopen(url)
content = html.read()
html.close()

l = []

soup = BeautifulSoup(content,"html5lib")
soup.prettify()

movies = soup.find_all("div",class_="intro")#get info from web

for items in movies:
    movie_name = items.a.get_text() #movie name
    movie_date = items.li.get_text()#display date

    str_movie_date = str(movie_date)
    str_movie_date = str_movie_date.replace('yue','/').replace('ri','/')

    movie_info = str_movie_date + movie_name
    n = ''.join(movie_info)
    m_list = []
    # if str_movie_date == day:
    #     today_movie = ''.join(n)
    #     print today_movie
    # else:
    #     str_movie_date.startswith(m)
    #     month_movie = ''.join(n)
    #     print month_movie

url2 = "http://movie.douban.com/nowplaying/shanghai/"
html2 = urllib2.urlopen(url2)
content2 = html2.read()
html2.close()

soup2 = BeautifulSoup(content2,"html5lib")


movie2 = soup2.find_all("li",class_="stitle")
for i in movie2:
    print i.a.get_text(),




"""邮件部分"""

msg1 = " 亲爱的xcsbaty，今天是%s等精彩电影上映的日子，希望你能喜欢！" % (n[6:20])
msg2 = """ which is so perfectly fitting for you!
                             #每天都永远爱你的汤姆猫！ """
msg3 = msg1+msg2
print msg3



"""email doc

import smtplib
from email.mime.text import MIMEText
mailto_list=["xcsbaty@21cn.com"]
mail_host="smtp.qq.com"  #设置服务器
mail_user="517xxxx93"    #用户名
mail_pass="amXXXX21"   #口令
mail_postfix="qq.com"  #发件箱的后缀

def send_mail(to_list,sub,content):
    me= "Dear xcsbaty"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='')
    msg['Subject'] = "亲爱的xcsbaty"
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,"hello",msg3):
        print "发送成功"
    else:
        print "发送失败"

        """

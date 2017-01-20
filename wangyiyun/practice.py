import requests
import bs4



url = 'http://music.163.com/#/playlist?id=5940079'
headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'Connection':'keep-alive',
    'Content-Length':'340',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'_ntes_nnid=c4f39453bde91ba65eb613f6031d79d5,1477642354623; _ntes_nuid=c4f39453bde91ba65eb613f6031d79d5; usertrack=ZUcIhVgWvvUPUg8OCI57Ag==; vjuids=-12351bb06.1581997fad7.0.7284f6079cff6; __utma=187553192.1159980154.1477885692.1479132856.1479132856.1; __utmz=187553192.1479132856.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __oc_uuid=9fb9eff0-aa74-11e6-846e-a1bb48bd6b52; nteslogger_exit_time=1480055459128; P_INFO=m15922860402@163.com|1480562480|0|other|00&99|not_found&1480525434&caipiao#shh&null#10#0#0|159402&1|caipiao&mail163|15922860402@163.com; __gads=ID=dbafcaffe88568cd:T=1481259283:S=ALNI_MZoPdhYseTA8t0BM_gtyz3AC4bRJQ; vjlast=1477898140.1484045023.11; vinfo_n_f_l_n3=2092373086990870.1.7.1477898140400.1481259640939.1484045366649; _ga=GA1.2.1159980154.1477885692; JSESSIONID-WYYY=0iS%5CGrSwCrGqJnYvsMKt8E%5CzT%2Bs8B9YvFtsm05Ywg%2FJmi6hrZ%2FxkiVIbkdiC93xZ5KFHnnlwP6rkPgRW4%2BYCsZZO107q9DzUXtY98pQwscxrM%2FqTUPA3G3V3KmiiNplGmDZ5NB%2B2dbEMDH%2FAlKtXapwA9Gp%2BKawnhE6PT%2BI1oSNGgoWf%3A1484744706773; _iuqxldmzr_=32; __utma=94650624.1159980154.1477885692.1484715155.1484742907.8; __utmb=94650624.8.10.1484742907; __utmc=94650624; __utmz=94650624.1484742907.8.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    'Host':'music.163.com',
    'Origin':'http://music.163.com',
    'Referer':'http://music.163.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
data1 = {
    'params':'Tak7nbc5FITyk0c2+nUtBBlxSnmr09QAM0C/QGw9kcpOYuIRx563RSwpF9FhlHBwA0EFIGxKlZl1i64eq8lJgXUXmiqI3YHfFKPJk7ufkEc=',
    'encSecKey':'002da1f54eec5b7d5aa3e4729679d2e8ef3a1d1d344e2454d2b5075210e4fd288a1904716341e8b53b58801df0f3cfb762299ec6a4e1d600790442e1fbbf63c5fd1ae8febf4274c84547e0b56ff460cbcca424b3de1f8566a34046248737dbad69308076d408a24829135f33d7334e7e1ab21bb31d2805974c07b37c9759d500'
}
def req(url):
    res = requests.get(url,headers=headers,data=data1)
    # print(res)
    ret = res.text
    # print(ret)
    soup = bs4.BeautifulSoup(ret)
    content = soup.find_all('textarea')
    print(content)
    with open('5940079.txt','w')as f:
        f.write(content)
    # return content

req(url)


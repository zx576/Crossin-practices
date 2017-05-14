import requests
a = 1

try:
    assert a == 1
    print('ok')
except:
    print('nok')

def verify_ip(dic):
    fixed_url = 'http://www.kuaidaili.com/free/inha/'
    try:
        res = requests.get(fixed_url, proxies=dic, timeout=1)
        assert res.status_code == 200
        return True
    except:
        return False


dic = {"http": "http://1.180.239.133:9999"}

# print(verify_ip(dic))

import pymongo

client = pymongo.MongoClient()
db = client.sixsix
proxies = db.proxies

def gen_dct():

    port_dct = {}
    for item in proxies.find():
        if item['port'] in port_dct.keys():
            port_dct[item['port']] += 1
        else:
            port_dct[item['port']] = 1


    # print(port_dct)
    result = [{'name':'其他','value':0}]
    for key,value in port_dct.items():
        res = {}
        if key == '端口号':
            continue
        if value < 10:
            result[0]['value'] += value
        else:
            res['name'] = key
            res['value'] = value
            result.append(res)

    for i in result:
        print("\'{}\'".format(i['value']),end=',')

    print('\n ===============  \n')
    for i in result:
        print("\'{}\'".format(i['name']),end=',')


gen_dct()

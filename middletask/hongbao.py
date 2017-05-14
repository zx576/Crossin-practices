import random

def getfen(yuan):
    return float(yuan) * 100


def fenqian(fen, jine):
    fenshu = int(fen)
    zongjine = float(jine)
    juntan = getfen(jine) / (fenshu + 1)
    listqian = []
    for x in range(fenshu):
        listqian.append(juntan)
    for y in range(fenshu - 1):
        edu = random.uniform(1, juntan - fenshu)
        listqian[y] = listqian[y] + edu
        juntan = juntan - edu
    listqian[-1] = listqian[-1] + juntan
    for z in range(fenshu):
        listqian[z] = listqian[z] / 100
    print("红包金额为" + str(zongjine) + ";共分为" + str(fenshu) + "个红包")
    print(str(list(listqian)))


fenqian(input("请输入红包份数"), input("请输入红包金额"))

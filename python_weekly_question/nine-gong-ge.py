

def arry1(N):
    for i in range(1,100):
        for j in range(i+1,100):
            if N-i-j > 0:
                yield [i,j,N-i-j]



def arry2(N,i):
    for m in range(1,100):
        if m in i:
            continue
        for n in range(m+1,100):
            if n in i or N-m-n in i or N-m-n < 0:
                continue
            yield [m,n,N-m-n]
# for i in arry1(N=50):
#     print(i)
#     for j in arry2(50,i):
#         print(j)
#     break

def arry3(N,i,j):
    q = N - i[0] - j[0]
    w = N - i[1] - j[1]
    e = N - i[2] - j[2]

    a3 = [q,w,e]
    for z in a3:
        if z <= 0 or z in i or z in j:
            return None

    as1 = [i[0],j[1],a3[2]]
    as2 = [i[2],j[1],a3[0]]


    if sum(a3) == N and sum(as1) == N and sum(as2) == N:
        return a3

    return None

def gene(N):
    res = []
    for i in arry1(N):
        # print(i)
        for j in arry2(N,i):
            # print(j)
            k = arry3(N,i,j)
            # print(k)
            if k:
                # print(k)
                res.append([i,j,k])

            else:
                continue

    return res


def main():
    n = int(input('>>>'))
    res = gene(n)
    if res:
        print(res)
        return res
    else:
        print('not found')
while 1:
    main()

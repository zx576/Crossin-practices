# coding=utf-8
# author = wuxiaojiao
# url = http://paste.ubuntu.com/25046101/

def Int_roman(n):
    st=("M","D","C","L","X","V","I")
    d=[1000,500,100,50,10,5,1]
    st1=""
    while n>0:
        d1=d+[n]
        d1.sort(reverse=True)
        n1=d1.index(n)
        l,m,r=(n1-1)/2*2,(n1-1)/2*2+1,(n1-1)/2*2+2
        if n<1000 and n/d[r]*d[r]==d[l]-d[r]:
            st1=st1+st[r]+st[l]
            n=n-(d[l]-d[r])
        elif n<1000 and n/d[r]*d[r]==d[m]-d[r]:
            st1=st1+st[r]+st[m]
            n=n-(d[m]-d[r])
        else:
            st1=st1+st[n1]*(n/d[n1])
            n=n%d[d1.index(n)]
    return st1

def romanToInt(m):
    st=("M","D","C","L","X","V","I")
    d=[1000,500,100,50,10,5,1]
    n=0
    for i in range(len(m)):
        if len(m)>1 and i<len(m)-1 and st.index(m[i])>st.index(m[i+1]):
            n=n-d[st.index(m[i])]
        else:
            n=n+d[st.index(m[i])]
    return n

assert romanToInt('III') == 3
assert romanToInt('IV') == 4
assert romanToInt('VI') == 6
assert romanToInt('XIX') == 19
assert romanToInt('XLV') == 45
assert romanToInt('MCMLXXX') == 1980
assert romanToInt('CMXCIX') == 999
# assert romanToInt('IM') != 999

# coding=utf-8
# author = 郑文杰 Willie
# url = http://paste.ubuntu.com/25047059/
def romanToInt(s):
    rv = dict(zip('IXCMVLD', (1, 10, 100, 1000, 5, 50, 500)))
    i = sum(-rv[a] if a in 'IXC' and rv[a]<rv[b] else rv[a] for a, b in zip(s, s[1:]+s[-1]))
    return i

assert romanToInt('III') == 3
assert romanToInt('IV') == 4
assert romanToInt('VI') == 6
assert romanToInt('XIX') == 19
assert romanToInt('XLV') == 45
assert romanToInt('MCMLXXX') == 1980
assert romanToInt('CMXCIX') == 999

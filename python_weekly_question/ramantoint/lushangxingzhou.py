#coding=utf-8
# author= 谢昇
# http://paste.ubuntu.com/25038134/
# http://paste.ubuntu.com/25038127/

def romanToInt2(s):
    """
    :type s: str
    :rtype: int
    """

    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    ans = 0
    size = len(s)
    i = 0
    while i < size:
        if i > 0 and d[s[i]] > d[s[i - 1]]:
            ans += d[s[i]] - 2 * d[s[i - 1]]
        else:
            ans += d[s[i]]
        i += 1
    return ans

def romanToInt(s):

    d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    res, p = 0, 'I'
    # 逆序逐一遍历
    # 使用逆序的好处在于，每次只需对一位罗马数字进行加或减的操作
    # 使用顺序的话，可能为两位
    for c in s[::-1]:
        if d[c] < d[p]:
            res = res - d[c]
        else:
            res = res + d[c]
        p = c

    return res


# assert romanToInt('III') == 3
# assert romanToInt('IV') == 4
# assert romanToInt('VI') == 6
# assert romanToInt('XIX') == 19
# assert romanToInt('XLV') == 45
assert romanToInt('MCMLXXX') == 1980
assert romanToInt('CMXCIX') == 999
assert romanToInt('') == 0

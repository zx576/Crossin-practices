# coding=utf-8
# author=淼
# url=paste.ubuntu.com/25044500

def romanToInt(s):
    d = {
        'I': 1,
        'X': 10,
        'C': 100,
        'M': 1000,
        'V': 5,
        'L': 50,
        'D': 500,
    }
    if len(s) == 1:
        i = d[s]
        return i
    i = 0
    n = 0
    while n < (len(s) - 1):
        _a = s[n]
        _b = s[n + 1]
        a = d[_a]
        b = d[_b]
        if a < b:
            i += b - a
            n += 1
        elif a >= b and n != len(s) - 2:
            i += a
        else:
            i += a + b
        n += 1
    return i


def int_to_roman(num):
    """
    num should be less equal than 3999
    """
    d = {
        '1': ('I', 'IV', 'V', 'IX'),
        '2': ('X', 'XL', 'L', 'XC'),
        '3': ('C', 'CD', 'D', 'CM'),
        '4': ('M'),
    }
    items = sorted(d.items())
    result = ''
    for item in items:
        num, mod_num = divmod(num, 10)
        str = ''
        if mod_num != 0:
            if item[0] != 4:
                if mod_num <= 3:
                    while mod_num > 0:
                        str = str.join(['', item[1][0]])
                        mod_num -= 1
                elif mod_num == 4:
                    str = item[1][1]
                elif mod_num == 5:
                    str = item[1][2]
                elif mod_num < 9:
                    str = item[1][2]
                    while mod_num > 5:
                        str = str.join(['', item[1][0]])
                        mod_num -= 1
                else:
                    str = item[1][3]
            else:
                while mod_num > 0:
                    str = str.join(['', item[1][0]])
                    mod_num -= 1
        result = str.join(['', result])

    return result


assert romanToInt('III') == 3
assert romanToInt('IV') == 4
assert romanToInt('VI') == 6
assert romanToInt('XIX') == 19
assert romanToInt('XLV') == 45
assert romanToInt('MCMLXXX') == 1980
assert romanToInt('CMXCIX') == 999
assert romanToInt('IM') != 999

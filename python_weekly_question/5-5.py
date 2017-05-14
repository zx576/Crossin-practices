

fenqi = 1633.11 * 12 - 18488

def shouyi(benjin,count=0):
    if count == 12:
        return benjin
    interest = benjin * 0.1 * 28 / 365
    count += 1
    benjin = benjin + interest - 1633.11
    return shouyi(benjin,count)


def shouyi2(benjin,count=0,stutas=1):
    # print(benjin)
    if count == 12:
        return benjin
    interest = benjin * 0.1 * 28 / 365
    count += 1
    if stutas == 1:
        benjin = benjin + interest - (18488/12) - 1109.28
        # print(benjin)
    else:
        benjin = benjin + interest - (18488/12)
    return shouyi2(benjin,count,stutas=0)

print(fenqi)
print(shouyi(18488))
# benjin = 18488-1109.28-(18488/12)
print(shouyi2(18488))

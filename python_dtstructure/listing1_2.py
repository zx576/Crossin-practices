
class Date:
    def __init__(self,month,day,year):
        self._jday = 0
        assert self.isvday(month,day,year),'invalid date'

        tmp = 0
        if month < 3:
            tmp = -1

        self._jday = day - 32075 + (1461 * (year + 4800 + tmp) // 4) + (367 * (month - 2 -tmp *12) // 12) - (3 * ((year + 4900 + tmp) // 100 ) // 4

    def month(self):
        return (self.tgday())[0]
    def day(self):
        return (self.tgday())[1]

    def year(self):
        return (self.tgday())[2]

    def dayofweek(self):
        month,day,year = self.tgday()
        if month < 3:
            month = month + 12
            year = year - 1

        return ((13 * month + 3 ) // 5 + day + \
                year + year//4  - year // 100  + year//400 ) % 7


    def __str__(self):
        month,day,year = self.tgday()

        return '{0}{1}{2}'.format(month,day,year)

    def __eq__(self,otherdate):
        return self._jday() == otherdate._jday()

    def __lt__(self,otherdate):
        return self._jday() > otherdate._jday()

    def __gt__(self,otherdate):
        return self._jday() < otherdate._jday()

    def tgday(self):
        a = self._jday + 68569
        b = 4 * a // 146097
        a = a - (146097 * b + 3) // 4
        year = 4000 * (a + 1) // 1461001
        a = a - (1461 * year // 4) + 31
        month = 80 * a // 2447
        day = a - (2447 * month // 80)
        a = month // 11
        month = month + 2 - (12 * a)
        year = 100 * (b - 49) + year + a
        return month, day, year

gd = Date(6,13,1993)
print(gt)

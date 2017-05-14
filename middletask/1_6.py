import datetime


class D_Time():

    def __init__(self, hours, minutes, seconds):
        self.time = self._get_time(hours, minutes, seconds)
        self.stamp = self._caculate()


    def _get_time(self, h, m, s):
        assert 0 <= h <= 23, 'invalid hours'
        assert 0 <= m <= 59, 'invalid minutes'
        assert 0 <= s <= 59, 'invalid seconds'

        return (h, m, s)

    def _caculate(self):
        stamp = 3600 * self.time[0] \
                + 60 * self.time[1] \
                + self.time[2]

        return stamp

    def _stamp2time(self,smp):
        hours = smp // 3600
        minutes = smp % 3600 // 60
        seconds = smp % 3600 % 60

        return (hours,minutes,seconds)

    def hour(self):
        return self.time[0]


    def minute(self):
        return self.time[1]


    def second(self):
        return self.time[2]


    def tostring(self):

        return '{0}:{1}:{2}'.format(self.time[0],self.time[1],self.time[2])


    def num_seconds(self,other_time):
        return self._caculate() - other_time._caculate()

    def is_am(self):
        return self.hour <= 12

    def is_pm(self):
        return self.hour > 12

    def comparable(self,other_time):
        return self._caculate() > other_time._caculate()



dt = D_Time(15,22,33)
dt2 = D_Time(13,22,46)

print(dt.num_seconds(dt2))

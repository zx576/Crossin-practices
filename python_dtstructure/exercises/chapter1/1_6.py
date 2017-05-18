

class Time_ADT:
    def __init__(self,h,m,s):

        assert isinstance(h,int) and isinstance(m,int) and isinstance(s,int)
        assert 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60

        self.time_lst = [h,m,s]

    def hours(self):
        return self.time_lst[0]

    def minutes(self):
        return self.time_lst[1]

    def seconds(self):
        return self.time_lst[2]

    def _time2seconds(self):
        return 3600*self.time_lst[0] + 60*self.time_lst[1] + self.time_lst[2]

    def _second2time(self,_seconds):
        hours = _seconds // 3600
        minutes = _seconds % 3600 // 60
        seconds = _seconds % 3600 % 60
        return [hours,minutes,seconds]

    def is_am(self):
        return self.time_lst[0] <= 12

    def time_delta(self,other_time):
        delta = abs(self._time2seconds() - other_time._time2seconds())
        time_lst = self._second2time(delta)
        return '{0}:{1}:{2}'.format(time_lst[0],time_lst[1],time_lst[2])

    def to_string(self):
        return '{0}:{1}:{2}'.format(self.time_lst[0],self.time_lst[1],self.time_lst[2])


mytime = Time_ADT(12,13,14)
mytime_2 = Time_ADT(8,13,14)

assert mytime.hours() == 12
assert mytime.minutes() == 13
assert mytime.seconds() == 14
assert mytime.is_am() == True
assert mytime.to_string() == '12:13:14'
print(mytime.time_delta(mytime_2))



class ClickCounter:

    def __init__(self):
        self.crt_count = 0

    def press(self):
        self.crt_count += 1
        return self.__str__()

    def reset(self):
        self.crt_count = 0
        return self.__str__()

    def __str__(self):
        print('current count is {0}'.format(self.crt_count))


clic = ClickCounter()

clic.press()
clic.reset()

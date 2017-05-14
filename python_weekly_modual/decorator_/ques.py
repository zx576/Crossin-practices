import time


def caculate(func):
    def input_func():
        start_time = time.ctime()
        print(start_time)
        func()
        end_time = time.ctime()
        print(end_time)

    return input_func


@caculate
def func():
    for i in range(100000):
        pass


func()

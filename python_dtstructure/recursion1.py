# coding=utf-8


def main():
    y = foo(3)
    print('=========')
    bar(3)


def foo(n):
    if n % 2 == 0:
        return 0
    else:
        print(n)
        return n + foo(n-1)


def bar(n):
    if n > 0:
        print(n)
        bar(n-1)


main()

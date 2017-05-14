#-*- coding:utf-8 -*-

class A():
    def __init__(self):
        pass

    def _method(self):
        print('this is single underscore')

    def print_method(self):
        self._method()

# a = A()
# a.print_method()
class B():
	def __method(self):
		print('this is double underscore')
# b = B()
# b.__method()

class C():
	def __init__(self):
		print('this is two underscore in the begining and end')

c = C()
# c.__she__()

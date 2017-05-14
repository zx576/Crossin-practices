

# def print_func(name):
#     return 'hello,'+ name
#
# func = print_func
#
# print(func('world'))

########################

# def prt_fun():
#     return 'hello,world'
#
# def call_func(func):
#     return func()
#
# print(call_func(prt_fun))


##############################

# def func_wrap():
#     def prt_func():
#         return 'hello,world'
#     return prt_func
#
# prt_hlowld = func_wrap()
# print(prt_hlowld())


# def func_wrap():
#     def prt_func(name):
#         return 'hello,'+name
#     return prt_func
#
# hlo = func_wrap()
# print(hlo('crossin'))


#
#
# def add_tag(func):
#     def prt_func(name):
#         return '<p>{0}</p>'.format(func(name))
#
#     return prt_func
#
# def print_text(name):
#     return 'hello,'+ name
#
# hlo = add_tag(print_text)
# print(hlo('crossin'))

###########################



# 定义一个嵌套函数，分别以函数和普通的字符串作为参数
# def add_tag(func):
#     def prt_func(name):
#         return '<p>{0}</p>'.format(func(name))
#     return prt_func

# # 定义一个普通的函数,并添加装饰器
# @add_tag
# def print_text(name):
#     return 'hello,'+ name
#
# print(print_text('crossin'))

# @add_tag
# def func1(word):
#     return 'arg is '+ word
#
# print(func1('abc'))
#######################################3
from functools import wraps
def add_tag(tagname):
    def decorator(func):
        @wraps(func)
        def prt_func(name):
            return '<{0}>{1}</{0}>'.format(tagname,func(name))
        return prt_func
    return decorator

@add_tag('div')
def print_text(name):
    return 'hello,'+name

print(print_text('crossin'))
print(print_text.__name__)

def func():
	pass

print(func.__name__)


# print(print_text('zx'))

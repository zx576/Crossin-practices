
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance   # nonlocal 非全局变量
        if amount > balance:
            return 'insuffcient funds'
        balance = balance - amount
        return balance

    return withdraw

# wd = make_withdraw(20)
# f = wd
# f(10)
# wd(5)
# print(f(10),wd(5))

# def mutable_link():
#     contents = empty
#     def dispatch(message,value=None):
#         nonlocal contents
#         if message == 'len':
#             return len_link(contents)
#
#         elif message == 'getitem':
#             return getitem_link(contents,value)
#         elif message == 'push_first':
#             return link(value,contents)
#         elif message == 'pop_first':
#             f = first()

def account(initial_amount):

    def deposite(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'insuffcient fund'
        dispatch['balance'] -= amount
        return dispatch['balance']

    dispatch = {
        'balance': initial_amount,
        'deposite': deposite,
        'withdraw': withdraw,
    }
    return dispatch

def withdraw(account,amount):
    return account['withdraw'](amount)
def deposite(account,amount):
    return account['deposite'](amount)

def check_balance(account):
    return account['balance']

# a = account(10)
#
# print(withdraw(a,15))


celsius = connector('celsius')
fahrenheit = connector('fahrenheit')

def converter(c,f):
    u,v,w,x,y = [connector() for _ in range(5)]
    multiplier(c,w,u)
    multiplier(v,x,u)
    adder(v,y,f)
    constant(w,9)
    constant(x,5)
    constant(y,32)

converter(celsius,fahrenheit)


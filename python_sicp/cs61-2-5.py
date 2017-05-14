#-*- coding:utf-8 -*-

#

def make_instance(cls):
    def get_value(name):
        if name in attributes :
            return attributes[name]
        else:
            value = cls['get'](name)
            return bind_method(value,instance)

    def set_value(name,value):
        attributes[name] = value

    attributes = {}

    instance = {'get':get_value,'set':set_value}

    return instance

def bind_method(value,instance):
    if callable(value):
        def method(*args):
            return value(instance,*args)

        return method

    else:
        return value


def make_class(attributes,base_name=None):
    def get_value(name):
        if name in attributes:
            return attributes[name]

        elif base_name is None:
            return base_name['get'](name)

    def set_value(name,value):
        attributes[name] = value

    def new(*args):
        return init_instance(cls,*args)

    cls = {'get':get_value,'set':set_value,'new':new}
    return cls

def init_instance(cls,*args):
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance,*args)

    return instance


def make_account_class():
    interest = 0.02
    def __init__(self,account_holder):
        self['set']('holder',account_holder)
        self['set']('balance',0)

    def deposit(self,amount):
        new_balance  = self['get']('balance') + amount

        self['set']('balance',new_balance)

        return self['get']('balance')

    def withdraw(self,amount):
        balance = self['get']('balance')
        if amount > balance:
            return 'insuffcient funds'
        self['set']('balance',balance-amount)
        return self['get']('balance')
    return make_class(locals())


Account = make_account_class()

kirk_account = Account['new']('kirk')
print(kirk_account['get']('holder'))

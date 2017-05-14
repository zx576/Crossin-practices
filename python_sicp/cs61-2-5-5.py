
class Account():
    interest = 0.02
    def __init__(self,account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            print('insufficient funds')
        self.balance = self.balance - amount
        return self.balance
class CheckingAccount(Account):
    interest = 0.01
    withdraw_charge = 1
    # def __init__(self,account_holder):
    #     super().__init__(account_holder)
    def withdraw(self,amount):
        return Account.withdraw(self,amount+self.withdraw_charge)

class SavingAccount(Account):
    deposit_charge = 2

    def deposit(self,amount):
        return Account.deposit(self,amount-self.deposit_charge)

class AsSeenOnTvAccount(CheckingAccount,SavingAccount):
    def __init__(self,account_holder):
        self.holder = account_holder
        self.balance = 1


che = CheckingAccount('sam')
print(che.deposit(10))
print(che.withdraw(5))
# print(che.b)
che.deposit(5)


# a = Account('xiaoz')
# print(a.balance)
# print(a.holder)
#
# a.deposit(100)
# print(a.balance)
# a.withdraw(50)
# print(a.balance)
#
# print(getattr(a,'balance'))
#
# print(hasattr(a,'withdraw'))
# print(type(a.deposit))
# print(type(Account.deposit))
# print(a.interest)
#
# b = Account('xiaol')
# b.interest = 0.08
# print(b.interest)
# print(a.interest)

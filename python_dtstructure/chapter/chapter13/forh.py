
class Parent:

    def __init__(self):

        self.num = 2
        print(self.num)

    def is_human(self):

        return True

class Child(Parent):

    def __init__(self):

        self.num = 1
        super(Parent,self).__init__()
        print(self.num)

c = Child()
print(c.is_human())

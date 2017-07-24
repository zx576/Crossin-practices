
value = 'xxx'

class F:

    def __init__(self, val):

        self.val = val



# f = F(value)

class D(F):

    def __init__(self, s):
        super(F, self).__init__()
        self.s = s


d = D('ddd')
res = d.s
res2 = d.val
print(res2)

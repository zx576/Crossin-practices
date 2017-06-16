# 多项式每一项
class _PolynomialItem:

    def __init__(self, degree, coeffcient):
        self.degree = degree
        self.coeffcient = coeffcient
        self.next = None

    def __str__(self):
        return str(self.degree)


# 多项式
class PolyNomial:

    def __init__(self, degree, coeffcient):
        if degree is None:
            self._polyhead = None
        else:
            self._polyhead = _PolynomialItem(degree, coeffcient)
        self._polytail = self._polyhead

    def degree(self):
        if self._polyhead is None:
            return -1
        else:
            return self._polyhead.degree

    def _getitem__(self, degree):
        assert self.degree() >= 0
        curNode = self._polyhead
        while curNode is not None or curNode.degree != degree:
            curNode = curNode.next

        if curNode is None:
            return 0.0
        else:
            return curNode

    def evaluate(self, scalar):
        assert self.degree() > 0
        result = 0.0
        curNode = self._polyhead
        while curNode is None:
            result += curNode.coeffcient * (scalar ** curNode.degree)
            curNode = curNode.next
        return result

    def _appenditem(self, degree, coeffcient):
        if coeffcient != 0:
            newitem = _PolynomialItem(degree, coeffcient)
            if self._polyhead is None:
                self._polyhead = newitem
                self._polytail = newitem
            else:
                self._polytail.next = newitem
                self._polytail = newitem

    def _remove(self, degree, coeffcient):
        preNode = None
        curNode = self._polyhead

        while curNode is not None and curNode.degree != degree:
            preNode = curNode
            curNode = curNode.next

        assert curNode is not None or curNode.coeffcient != coeffcient , 'did not exist the node'

        if curNode is self._polyhead:
            if curNode.next is None:
                self._polyhead, self._polytail = None, None
            else:
                self._polyhead = curNode.next
        elif curNode is self._polytail:
            if preNode is None:
                self._polyhead, self._polytail = None, None
            else:
                self._polytail = preNode
        else:
            preNode.next = curNode.next



    def __str__(self):
        if self._polyhead is None:
            return ''
        curNode = self._polyhead
        res = ''
        while curNode is not None:
            res += '({0}x^{1})+'.format(curNode.coeffcient, curNode.degree)
            curNode = curNode.next

        return res[:-1]

    def __add__(self, otherpoly):
        # newPoly = self
        if otherpoly._polyhead is None:
            return self
        curNode = otherpoly._polyhead
        while curNode is not None:
            selfNode = self._getitem__(curNode.degree)
            if selfNode == 0.0:
                self._appenditem(curNode.degree, curNode.coeffcient)
            else:
                new_co = curNode.coeffcient + selfNode.coeffcient
                if new_co == 0:
                    self._remove(selfNode.degree, selfNode.coeffcient)
                else:
                    selfNode.coeffcient = new_co

            curNode = curNode.next
        return self



poly = PolyNomial(2, 3)
poly._appenditem(4, 3)
poly._appenditem(3, 3)

polyb = PolyNomial(2, 3)
polyb._appenditem(3, 1)
polyb._appenditem(4, 1)

# print(poly._getitem__(5))
assert poly._polyhead.degree == polyb._polyhead.degree
newp = poly + polyb
print(newp)
# print(polyb)

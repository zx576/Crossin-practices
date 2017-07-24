# coding=utf-8
# date=2017.7.10

# description
# 二叉树

from operator import *
import queue

class _ExpTreeNode:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class ExpressionTree:

    def __init__(self, expstr):
        self._expTree = None
        self._buildTree(expstr)

    def evaluate(self, varMap):
        return self._evalTree(self._expTree, varMap)

    def __str__(self):
        return self._buildString(self._expTree)

    def _buildString(self, treeNode):
        if treeNode.left is None and treeNode.right is None:
            return str(treeNode.value)
        else:
            expTree += '('
            expTree += self._buildString(treeNode.left)
            expTree += str(treeNode.value)
            expTree += self._buildString(treeNode.right)
            expTree += ')'

        return expTree

    def _evalTree(self, subtree, varDict):

        # independent branch
        if subtree.left is None and subtree.right is None:
            if subtree.value.isdigit():
                return int(subtree.value)

            else:
                assert subtree.value in varDict
                return varDict[subtree.value]

        # operator
        else:
            lval = self._evalTree(subtree.left)
            rval = self._evalTree(subtree.right)
            return _compute(lval, rval, subtree.value)

    def _compute(self, left, right, op):
        op_dispatch = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div,

        }
        assert op in op_dispatch
        return op_dispatch[op](left, right)

    def _buildTree(self, expstr):

        expQ = queue.Queue()
        for token in expstr:
            expQ.put(token)

        self._expTree = _Node(None)
        self._reBuildTree(self._expTree, expQ)

    def _reBuildTree(self, curnode, expQ):

        token = expQ.get()
        if token == '(':
             curnode.left = _Node(None)
             pass


e = ExpressionTree('sss ')
res = e._compute(1,3,'+')
print(res)

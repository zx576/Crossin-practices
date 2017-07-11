# coding=utf-8
# date=2017.7.10

# description
# 二叉树

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

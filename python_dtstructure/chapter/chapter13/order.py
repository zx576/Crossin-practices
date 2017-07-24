# coding=utf-8
# author = zhouxin
# date = 2017.7.16

class _Node:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.val = value


class BinaryTree:

    def __init__(self):

        self.begin = _Node(1)
        self.scale = 5
        self.build()
        # print(self.begin.left.val)

    def _re_build(self, node):
        if node.val > 10:
            return
        node.left, node.right = _Node(node.val*2), _Node(node.val*2)
        self._re_build(node.left)
        self._re_build(node.right)

    # 创建一个满二叉树
    def build(self):
        return self._re_build(self.begin)

    # 先序遍历
    def _preorder(self, node):
        if node is not None:
            print(node.val)
            self._preorder(node.left)
            self._preorder(node.right)

    def preorder(self):
        return self._preorder(self.begin)

    # 中序遍历
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.val)
            self._inorder(node.right)

    def inorder(self):
        return self._inorder(self.begin)

    # 后序遍历
    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.val)

    def postorder(self):
        return self._postorder(self.begin)

    # 宽度遍历 
    def breadthorder(self):

        lst = [self.begin,]
        for node in lst:
            if node.left is not None:
                lst.append(node.left)
            if node.right is not None:
                lst.append(node.right)

            print(node.val)




b = BinaryTree()
# b.build()
# b.preorder()
# b.inorder()
# b.postorder()
b.breadthorder()

## 二叉树 4 种排序方式

二叉树结点代码

```python
class _Node:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.val = value

```

先序遍历

```python
class BinaryTree:
    # ...
    # 先序遍历
    def _preorder(self, node):
        if node is not None:
            print(node.val)
            self._preorder(node.left)
            self._preorder(node.right)


```

中序遍历

```python

class BinaryTree:
    # ...
    # 中序遍历
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.val)
            self._inorder(node.right)

```

后续遍历

```python
class BinaryTree:
    # ...
    # 后序遍历
    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.val)

```

前三种遍历看起来只是微调了代码顺序，但由于是基于递归调用,产生的结果大不相同。

宽度遍历
```python
class BinaryTree:
    # ...
    # 宽度遍历
    def breadthorder(self):

        lst = [self.begin,]
        for node in lst:
            if node.left is not None:
                lst.append(node.left)
            if node.right is not None:
                lst.append(node.right)

            print(node.val)

```

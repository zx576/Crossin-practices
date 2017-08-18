## 旋转矩阵

#### 题目说明

给定一个　n * n 的矩阵，将其顺时针旋转 90°．输出处理之后的矩阵

举例：　

１　２　３　　　　　　7　4　1

４　５　６　　-> 　　　8　5　2

７　８　９　　　　　　9　6　3　


#### 附加题

在不定义额外的变量的情况下做变换，即，所有的变换都基于原矩阵．


```python

def ratate(matrix):
    '''
    : type matrix : List(List(Int))
    : rtype: List(List(Int))
    '''

    # your code here

m1 = [[]]
m2 = [[1]]
m3 = [[i for i in range(3)] for j in range(3)]
m4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

assert ratate(m1) == [[]]
assert ratate(m2) == [[1]]
assert ratate(m3) == [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
assert ratate(m4) == [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

```

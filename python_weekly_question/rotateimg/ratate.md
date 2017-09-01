## 旋转矩阵

#### 题目说明

给定一个　n * n 的矩阵，将其顺时针旋转 90°．输出处理之后的矩阵

举例：　

１　２　３　　　　　　7　4　1

４　５　６　　-> 　　　8　5　2

７　８　９　　　　　　9　6　3　


#### 附加题

在不定义额外的变量的情况下做变换，即，所有的变换都基于原矩阵．


#### 解释

该题目存在一行代码的简单解法, 如下所示,将矩阵逆序处理之后再转置即可.直接理解起来可能有些困难,纸上演算一下可能会好一点.

```python

def rotate(matrix):
    '''
    : type matrix : List(List(Int))
    : rtype: List(List(Int))
    '''

    return zip(*matrix[::-1])

```

另外一种理解起来稍微容易,但代码看起来就相对复杂了,如下所示,思路是一次性对 4 个位置进行交换,如题目中所给的矩阵所示, 四个角的数字分别为 [1,3,9,7] 交换后为 [7,1,3,9], 如此循环,逐层处理, 最后得到结果

```python

def rotate2(matrix):

  length = len(matrix)
    for i in range(int(length/2)):
        count = 0
        for j in range(i,length-1-i):
            # [1,3,9,7] --> [7,1,3,9]
            matrix[i][j], matrix[i+count][length-i-1], matrix[length-i-1][length-j-1], matrix[length-j-1][i] = \
            matrix[length-j-1][i], matrix[i][j], matrix[i+count][length-i-1], matrix[length-i-1][length-j-1]

            count += 1
    return matrix



m1 = [[]]
m2 = [[1]]
m3 = [[i for i in range(3)] for j in range(3)]
m4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

assert rotate(m1) == [[]]
assert rotate(m2) == [[1]]
assert rotate(m3) == [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
assert rotate(m4) == [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

```

除了以上两种方法,其他同学也提出了不同的解决方案
cheng_y￼ 同学的答案采用了两两换位的方式:　https://paste.ubuntu.com/25345391/
王凌鸿￼　同学的思路和cheng_y￼相似：　https://paste.ubuntu.com/25339267/
jzy丶同学使用了numpy 来解决： https://github.com/Noir-desir/every-weekend/blob/master/matrix.py
其他诸如　strawhat￼，　聂宇威￼　也很好的完成的作业

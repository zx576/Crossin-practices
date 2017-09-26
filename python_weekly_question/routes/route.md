## 找路径


现有一个 m × n (m,n 都小于 100)的网格，位于左上角的 A 要去寻找右下角的 B，A 只能向下或者向右行走，现在问题来了，按照刚才的规则，A 到达 B 一共有多少种不重复的路径？


![](Selection_182.png)



解决思路

当该矩阵为 2 * 2 时

```
A A-left
A-down B
```

A 到 B 的路劲可分解为 A-left 到 B 与 A-down 到 B 之和。如下所示：

```
2  1
1  0 
```

当为 3 * 3　时：

```
6 3 1
3 2 1
1 1 1

```

认识到这一点之后，代码就水到渠成了。
鉴于答案区多数同学使用的是递归方法和数学方法，这里我们先给出一个迭代版本供参考：

```python

def uniquePath(m, n):
    '''
    :type m: int
    :type n: int
    :rtype: int
    '''

    matrix = [[1 for i in range(m)] for j in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

    return matrix[-1][-1]
    
assert uniquePath(1, 2) == 1
assert uniquePath(3, 3) == 6
assert uniquePath(10, 20) == 6906900

```

然后是递归版本,参考的是 `elyt` 同学的代码：

```python
def uniquePath(m, n):
    '''
    :type m: int
    :type n: int
    :rtype: int
    '''
    if (m==1) or (n==1):
        return 1
    else:
        return uniquePath(m,n-1)+uniquePath(m-1,n)

```

最后是纯数学版本，参考了 `LDJ` 同学的代码：

```python
import math

def uniquePath(m,n):
	return ((math.factorial(m+n-2))/((math.factorial(m-1))*(math.factorial(n-1))))

```


使用了递归方法的同学有：

elyt￼：　https://paste.ubuntu.com/25593211/

狮子不咬人：　https://paste.ubuntu.com/25604140/

bolin：　https://paste.ubuntu.com/25591094/

数学方法：
LDJ￼：https://github.com/NyanCat12/CrossinWeekly/blob/master/20170922/0922.py

其他方法：
王炎：　https://paste.ubuntu.com/25606404/
还有未给出代码地址，仅仅口述了方法的同学就不一一提了。


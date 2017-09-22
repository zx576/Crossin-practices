## 找路径


现有一个 m × n (m,n 都小于 100)的网格，位于左上角的 A 要去寻找右下角的 B，A 只能向下或者向右行走，现在问题来了，按照刚才的规则，A 到达 B 一共有多少种不重复的路径？


![](Selection_182.png)


```python

def uniquePath(m, n):
    '''
    :type m: int
    :type n: int
    :rtype: int
    '''

    # your code here


assert uniquePath(1, 2) == 1
assert uniquePath(3, 3) == 6
assert uniquePath(10, 20) == 6906900


```



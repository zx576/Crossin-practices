# coding=utf-8

# 迭代法
def binarysearch(lst, key):

    start = 0
    end = len(lst)-1

    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == key:
            return True
        elif lst[mid] > key:
            end = mid -1
        else:
            start = mid + 1

    return False

# lst = list(range(10))
# key = 5
#
# res = binarysearch(lst, key)
# print(res)

# 递归法
def re_binary(lst, key, start, end):
    if start > end:
        return False
    mid = (start+end)//2
    if lst[mid] == key:
        return True
    elif lst[mid] > key:
        return re_binary(lst, key, start, mid-1)
    else:
        return re_binary(lst, key, mid+1, end)

lst = list(range(10))
key = 50
start = 0
end = len(lst)-1

res = re_binary(lst, key, start, end)
print(res)

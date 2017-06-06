# coding : utf-8

lst = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

def binary_search(lst,value):
    start = 0
    end = len(lst) - 1
    while True:
        mid = (start + end) // 2
        # print(lst[mid])
        if lst[mid] == value:
            return True

        if lst[mid] > value:
            end = mid - 1

        else:
            start = mid + 1

        # print(lst[start:end+1])

    return False


print(binary_search(lst,13))

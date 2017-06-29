# coding=utf-8

s = [0,1,2,3,4,5,6,7,8,9]
t = 10

def recBinarySearch(target, seq, first, end):
    print(first,end)
    if first > end:
        return False
    else:
        mid = (first+end)//2
        print(mid)
        if seq[mid] == target:
            return True
        elif target > seq[mid]:
            return recBinarySearch(target, seq, mid+1, end)
        else:
            return recBinarySearch(target, seq, first, mid-1)


res = recBinarySearch(t,s,0,len(s)-1)
print(res)

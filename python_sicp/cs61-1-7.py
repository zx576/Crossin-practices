

def count_partitions(n,m):
    if m == 0:
        return 0
    elif n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        # print((n-m,m),(n,m-1))
        # print(count_partitions(n-m,m) + count_partitions(n,m-1))
        return count_partitions(n-m,m) + count_partitions(n,m-1)

print(count_partitions(6,4))

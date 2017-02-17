
def maxn(args):
    # print(args)
    if len(args) == 1:
        return args
    max_int = args[0]
    for i in args[1:]:
        if i > max_int:
            max_int = i

    return max_int

a = (1,2,3,4,-9)
print(maxn(a))

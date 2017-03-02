from operator import mul,add

pair = [[1,2],[2,3],[3,4],[4,5]]
for i,j in pair:
    print(i,j)

print(type(pair))

print(type(range(4)))

#  2-3-3



# print(divisors(12))
#
# perfect_int = [x for x in range(1,1001) if sum(divisors(x))==x]
# print(perfect_int)


def divisors(n):
    return [1]+[x for x in range(2,n) if n%x==0]

print(divisors(12))
# >>>[1, 2, 3, 4, 6]

def width(area,height):
    assert area % height == 0
    return area // height

print(width(80,16))
# >>>5

def perimeter(width,height):
    return (width+height)*2

def minium_perimeter(area):
    height = divisors(area)
    perimeters = [perimeter(width(area,h),h) for h in height]
    return min(perimeters)


print(minium_perimeter(80))


def apply_to_all(map_fn,s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn,s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn,s,initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced,x)
    return reduced

# print(reduce(mul,[2,4,8],1))
def divisors_of(n):
    divided_n = lambda x:n%x ==0
    return [1]+keep_if(divided_n,range(2,n))

print(divisors_of(12))

def sum_of_divisors(n):
    return reduce(add,divisors_of(n),0)

def perfect_n(n):
    return sum_of_divisors(n) == n

print(keep_if(perfect_n,range(1,1000)))

keep_if_2 = lambda filter_fn,s:list(filter(filter_fn,s))

##################

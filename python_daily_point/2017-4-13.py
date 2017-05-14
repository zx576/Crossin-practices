# 
l = [1,1,2,2,3,3,4,5,5,6,6]

# set_l = set(l)
#
# for i in set_l:
#     if l.count(i) == 1:
#         print(i)

def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    start = 0; end = len(nums) - 1; mid = (start + end) // 2

    while start <= end:
        mid = (start + end) // 2; is_even_position = mid % 2 == 0

        if (mid == 0 or nums[mid] != nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] != nums[mid+1]):
            return nums[mid]
        elif mid == len(nums) - 1 or nums[mid] == nums[mid + 1]:
            if is_even_position:
                start = mid + 1
            else:
                end = mid - 1
        elif mid == 0 or nums[mid] == nums[mid - 1]:
            if is_even_position:
                end = mid - 1
            else:
                start = mid + 1


    return -1


print(singleNonDuplicate(l))

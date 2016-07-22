import math


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    lngth = len(nums)
    i = 0
    j = 0
    while i < lngth and j < lngth:
        if nums[i] == val:
            if j == 0:
                j = i + 1
            while j < lngth:
                if nums[j] !=val:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                    break
                else:
                    j += 1
        else:
            i += 1

    return i

print(removeElement([2,2], 4))
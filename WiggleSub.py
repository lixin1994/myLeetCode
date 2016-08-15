def wiggleMaxLength( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    isNeg = 0
    result = 1
    k = True
    for i,n in enumerate(nums[1::]):
        if isNeg == -1:
            if n > nums[i]:
                result += 1
                isNeg = 1
        elif isNeg == 1:
            if n < nums[i]:
                result += 1
                isNeg = -1
        else:
            if n > nums[i]:
                result += 1
                isNeg = 1
            elif n < nums[i]:
                result += 1
                isNeg = -1
    return result

print(wiggleMaxLength([1,2,2,2,1,0,2,2,2,6]))
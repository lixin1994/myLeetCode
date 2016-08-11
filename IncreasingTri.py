def increasingTriplet( nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dct = [1 for i in range(0, len(nums))]
    for i, j in enumerate(nums):
        for p, k in enumerate(nums[0:i]):
            if j > k:
                if dct[p] == 2:
                    return True
                else:
                    if dct[i] == 1:
                        dct[i] += 1
    return False

print([1,2,3,4] == [3,2,1,4])
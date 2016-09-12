def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    result = [[]]
    for i in nums:
        result += [k + [i] for k in result if k + [i] not in result]
    return result

print(subsetsWithDup([1,2,2]))
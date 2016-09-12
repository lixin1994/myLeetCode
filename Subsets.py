def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return [[]]
    return [i + [nums[-1]] for i in subsets(nums[0:len(nums)-1])] + [i for i in subsets(nums[0:len(nums)-1])]

print( subsets([1,2,3]))
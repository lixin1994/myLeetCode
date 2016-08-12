def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums) - 1
    def bSch(low, high, nums, target):
        if low > high:
             return -1
        mid = (high + low) // 2
        if target  == nums[mid]:
            return True
        if nums[low] < nums[high]:
            if target > nums[mid]:
                return bSch(mid + 1, high, nums,target)
            else:
                return bSch(low, mid - 1, nums,target)
        if nums[mid] <= nums[high]:
            if target < nums[mid] or target >= nums[low]:
                return bSch(low, mid - 1, nums, target)
            else:
                return bSch(mid + 1, high, nums, target)
        else:
            if target > nums[mid] or target <= nums[high]:
                return bSch(mid + 1, high, nums,target)
            else:
                return bSch(low, mid - 1, nums,target)
    return bSch(low, high, nums, target)

print(search([3,1,1], 3))
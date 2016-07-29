def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = 1
        length = len(nums)
        while j < length:
            while j < length and nums[i] == nums[j]:
                j += 1
            if j < length:
                nums[i + 1] = nums[j]
                j+=1
            else:
                break
            i += 1
        return i+1

print(removeDuplicates([1,1]))
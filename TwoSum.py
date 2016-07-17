def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        liter = 0;
        tempdict = dict()
        for i in nums[:]:


            if((target-i) in tempdict):
                return [tempdict[target-i], liter]
            tempdict[i] = liter
            liter+=1

nums = [1,2,3,4,5]
print(twoSum(nums, 9))

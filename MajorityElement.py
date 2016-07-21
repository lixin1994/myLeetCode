import collections


def majorityElement(nums):
    return collections.Counter(nums).most_common(1)[0][0]


print(majorityElement([1,2,3,1,2,1]))
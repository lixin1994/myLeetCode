class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.total = 0


class NumArray(object):

    def __init__ (self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """

        def createTree(nums, l, r):
            if l > r:
                return None
            elif l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n

            mid = (l + r)//2


            root = Node(l, r)
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)
            root.total = root.left.total + root.right.total
            return root

        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        def updateFun(root, i, val):
            mid = (root.end + root.start) // 2
            if root.start == i and root.end == i:
                root.total = val
                return root.total
            if i <= mid:
                root.total = root.total - root.left.total + updateFun(root.left, i, val)
                return root.total
            else:
                root.total = root.total - root.right.total + updateFun(root.right, i, val)
                return root.total

        updateFun(self.root, i, val)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            mid = (root.start + root.end) // 2
            if i >= mid + 1:
                return rangeSum(root.right, i, j)
            elif j <= mid:
                return rangeSum(root.left, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)

        return rangeSum(self.root, i, j)


nums = [1, 3, 5]

na = NumArray(nums)
print(na.sumRange(0, 1))
na.update(1, 2)
print(na.sumRange(0, 2))

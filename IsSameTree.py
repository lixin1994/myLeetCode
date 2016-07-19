class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p != None and q != None:

            if p.val == q.val and isSameTree(self, p.left, q.left) and isSameTree(self, p.right, q.right):
                return True
            else:
                return False
        else:
            return False


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root == None:
        return False

    if root.val == sum and root.left == None and root.right == None:
        return True
    elif root.val < sum:
        return False
    else:
        return hasPathSum(root.left, sum - root.val) or \
           hasPathSum(root.right, sum - root.val)

a = TreeNode(1)
b = TreeNode(2)
a.right = b

print(hasPathSum(a,3))
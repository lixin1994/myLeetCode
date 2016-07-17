def maxDepth(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [(root, 1)]
        if len(root) == 0:
            return 0
        MaxDepth = 1
        while stack:
            temp = stack.pop(-1)
            troot = temp[0]
            depth = temp[1]
            if depth > MaxDepth:
                MaxDepth = depth
            if troot.left != None:
                stack.append((troot.left, depth + 1))
            if troot.right != None:
                stack.append((troot.right, depth + 1))
        return MaxDepth

a=[]

print(maxDepth(a))
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    mid = len(height) // 2
    result = 0
    left = [(0, height[0])]
    right = [(len(height) - 1, height[-1])]
    maxleft = height[0]
    maxright = height[-1]
    for i in range(1, mid + 1):
        if height[i] > maxleft:
            maxleft = height[i]
            left.append((i, height[i]))
        if height[- i - 1] > maxright:
            maxleft = height[i]
            right.append((len(height) - i - 1, height[- i - 1]))
    return max([(k[0] - j[0]) * min(j[1], k[1]) for j in left for k in right])
print(maxArea([1,2,3,3,2,1,6,4,2,1]))
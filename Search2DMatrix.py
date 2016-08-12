def searchMatrix( matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    def BSearch(matrix, target, start, end):
        if end < start:
            return False
        mid = (end + start) // 2
        length = len(matrix[0])
        row = mid // len(matrix[0])
        column = mid % len(matrix[0])
        midval = matrix[row][column]
        if midval == target:
            return True
        elif midval < target:
            return BSearch(matrix, target, mid + 1, end)
        else:
            return BSearch(matrix, target, start, mid - 1)
    num = len(matrix) * len(matrix[0])
    return BSearch(matrix, target, 0, num - 1)
print(searchMatrix( [[1],[3]], 2))
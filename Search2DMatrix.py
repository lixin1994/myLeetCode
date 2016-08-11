def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    def BSearch(matrix, target, start, end):
        mid = (end + start) // 2
        midval = matrix[mid // len(matrix[0])][mid % len(matrix)]
        if midval == target:
            return True
        if end == start:
            return False
        elif midval > target:
            return BSearch(matrix, target, mid + 1, end)
        else:
            return BSearch(matrix, target, start, mid - 1)
    num = len(matrix) * len(matrix[0])
    return BSearch(matrix, target, 0, num - 1)
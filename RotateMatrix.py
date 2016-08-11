def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    length = len(matrix)
    for i in range(0, length):
        for j in range(0, length - i):
            matrix[i][j], matrix[length - 1 - j][length - 1 - i] = matrix[length - 1 - j][length - 1 - i],matrix[i][j]
    for i in range(0, length // 2):
        for j in range(0, length):
            matrix[i][j], matrix[length - 1 - i][j] = matrix[length - 1 - i][j], matrix[i][j]
    for temp in matrix:
        print (temp)
rotate([[1,2,3],
        [4,5,6],
        [7,8,9]])
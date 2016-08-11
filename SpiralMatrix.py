def generateMatrix( n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        xStart, xEnd, yStart, yEnd = 0, n, 0, n
        result= [ [ 0 for i in range(n) ] for j in range(n) ]
        num, row, column =1, 0, 0
        while num <= n ** 2:
            for i in range(xStart, xEnd):
                result[row][column] = num
                num += 1
                column += 1
            row += 1
            yStart += 1
            column -= 1
            for i in range(yStart, yEnd):
                result[row][column] = num
                num += 1
                row += 1
            column -= 1
            xEnd -= 1
            row -= 1
            for i in range(xStart, xEnd):
                result[row][column] = num
                num += 1
                column -= 1
            column += 1
            yEnd -= 1
            row -= 1
            for i in range(yStart, yEnd):
                result[row][column] = num
                num += 1
                row -= 1
            column += 1
            xStart += 1
            row += 1
        return result
print(generateMatrix(4))
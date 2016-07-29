def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    result = [[1]]
    for n in range(1, numRows):
        bef = result[n-1]
        line = []
        for m in range(0, n + 1):
            if m == 0 or m == n:
                line.append(1)
            else:
                line.append(bef[m-1]+bef[m])
        result.append(line)
    return result

print(generate(0))
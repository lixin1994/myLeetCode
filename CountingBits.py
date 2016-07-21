def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    i = 0
    result = [0]
    count = 1
    for j in range(1, num+1):

        if i != 0 and j % (2**i) == 0:
            i += 1
            count = 1
        if (j % (2**i)) % 2 == 1:
            count += 1
        if i == 0:
            i += 1
        result.append(count)

    return result

print(countBits(8))
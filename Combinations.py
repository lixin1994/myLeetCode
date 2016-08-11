def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    def comb(n, k):
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if n == k:
            return [[i for i in range(1, n+1)]]
        return [i + [n] for i in comb(n-1,k-1)] + [i for i in comb(n-1, k)]
    return comb(n, k)

print(combine(4,3))
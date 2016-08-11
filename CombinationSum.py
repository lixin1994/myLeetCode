def combinationSum(candidates, target):
    dp = []
    for i in range(0, target + 1):
        dp.append([])
        for j in candidates:
            if i >= j:
                if i == j:
                    dp[i].append([j])
                else:
                    for k in dp[i-j]:
                        if k:
                            t = sorted(k + [j])
                            if not t in dp[i]:
                                dp[i].append(t)

    return dp[target]

print(combinationSum([2,3,6,7],7))
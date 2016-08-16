def flaten(nList):
    res = []
    for l in nList:
        if type(l) == type([]):
            res += flaten(l)
        else:
            res.append(l)
    return res

print(flaten([[1,2],3,[4,5]]))
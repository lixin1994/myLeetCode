def search(start, end, target):
    mid = (start + end) // 2
    if mid ** 2 == target or mid ** 2 < target :
        return mid
    elif mid ** 2 < target:
        return search(mid + 1, end, target)
    else:
        return search(start, mid - 1, target)

print(search(0,2,2))
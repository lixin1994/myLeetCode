def IntAdd(a, b):
    if not a or not b:
        return a or b
    else:
        return IntAdd((a & b) << 1, a ^ b)


def getSum(a, b):
    if a*b<0:
        if IntAdd(~a, 1) == b:
            return 0
        elif IntAdd(~a, 1) > b:
            return IntAdd(a, b)
        else:
            return IntAdd(~IntAdd(IntAdd(~a, 1), IntAdd(~b, 1)), 1)
    else:
        return IntAdd(a, b)


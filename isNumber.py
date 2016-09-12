def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    ecount = 0
    dotcount = 0
    def isValid(single):
        if 47 < ord(single) < 58 or ord(single) == 46 or single == 'e':
            return True
        else:
            return False
    i = 0
    j = len(s)-1
    bef1 = ' '
    bef2 = ' '
    if j == 0 and s[0] == '.':
        return False
    while j >= i:
        while s[i] == ' ' and j > i:
            if not isValid(bef1):
                i += 1
                bef1 = ' '
            else:
                return False
        while s[j] == ' ' and j > i:
            if not isValid(bef2):
                j -= 1
                bef2 = ' '
            else:
                return False

        if s[i] == '.':
            if dotcount == 1:
                return False
            dotcount += 1

        if s[i] == '.' and i != j:
            if dotcount == 1:
                return False
            dotcount += 1

        if s[i] == 'e':
            if bef1 == ' ':
                return False
            if ecount == 1:
                return False
            ecount += 1
        if s[j] == 'e' and  i != j:
            if bef1 == ' ':
                return False
            if ecount == 1:
                return False
            ecount += 1
        if not isValid(s[i]):
            return False
        if not isValid(s[j]):
            return False
        bef1 = s[i]
        bef2 = s[j]
        i += 1
        j -= 1

    return True
print(isNumber('21..1'))
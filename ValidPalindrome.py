def isPalindrome(s):

    i = 0
    j = len(s)-1
    while j > i:
        while not s[j].isalnum() and j > i:
            j -= 1
        while not s[i].isalnum() and j > i:
            i += 1

        if s[j].upper() != s[i].upper():
            return False

        i += 1
        j -= 1

    return True

print(isPalindrome('12321'))
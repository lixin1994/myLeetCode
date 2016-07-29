
def getHint(secret, guess):
    """
    :type secret: str
    :type guess: str
    :rtype: str
    """
    A = 0
    B = 0
    BList = []
    for c1, c2 in zip(secret, guess):
        if c1 == c2:
            A += 1
            secret = secret.replace(c1, '')
            guess.replace(c1, '')
    for c1, c2 in zip(secret, guess):
        if c2 in secret:
            B += 1
            secret.replace(c2, '')
            guess.replace(c2, '')
    return str(A) + 'A' + str(B) + 'B'

print(getHint("12312312345123","12345121234564"))
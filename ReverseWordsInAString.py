import re

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    re.split(' +', s)
    words = s.split(' ', )
    reverseS = ''
    n = len(words)

    if words[0] == '':
        if n == 1:
            return "";
        words.remove('')
        n -= 1

    while n > 0:
        n -= 1
        if words[n] == '' and n == 0:
            continue
        reverseS += words[n] + ' ';
    reverseS += words[n]
    return reverseS

print('[' + reverseWords(' 1 2 3')+']')
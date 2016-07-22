def reverseVowels(s):
        """
        :type s: str
        :rtype: str
        """
        def isVowels(char):
            if char == 'a' or char == 'e' or char =='i' or char =='o' or char == 'u':
                return True
            return False
        i = 0
        j = len(s)-1
        slist = list(s)
        while j > i:
            while not isVowels(slist[i].lower()) and j > i:
                i += 1
            while not isVowels(slist[j].lower()) and j > i:
                j -= 1
            slist[i], slist[j] = slist[j], slist[i]
            i += 1
            j -= 1
        return ''.join(slist)

print(reverseVowels("aeiouA"))
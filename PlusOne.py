def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        up = 1
        i = len(digits)-1
        while up == 1:
            if i == -1:
                app = [1]
                app.extend(digits)
                digits = app
                break
            temp = digits[i] + up
            digits[i] = temp % 10
            up = temp//10
            i -= 1
        return digits

print(plusOne([9]))
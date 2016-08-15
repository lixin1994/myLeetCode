def isValidSerialization(preorder):
    """
    :type preorder: str
    :rtype: bool
    """
    prelist = preorder.split(",")
    stack = []
    for i in prelist:
        stack.append('#')
        while len(stack) >= 3 and stack[len(stack) - 1] == '#' and stack[len(stack) - 2] == '#':
            for i in range(0, 3):
                stack.pop()
            stack.append('#')

    return len(stack) != 0 and stack[0] == '#'

print(isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
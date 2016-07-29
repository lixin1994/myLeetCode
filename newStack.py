from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        newData = deque()
        size = len(self.data)
        i = 0

        while i < size - 1:
            newData.append(self.data.popleft())
            i += 1
        while self.data:
            self.data.popleft()
        while newData:
            self.data.append(newData.popleft())



    def top(self):
        """
        :rtype: int
        """
        newData = deque()
        temp = None
        while self.data:
            temp = self.data.popleft()
            newData.append(temp)
        while newData:
            self.data.append(newData.popleft())
        return temp

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.data) == 0:
            return True
        else:
            return False

s = Stack()
s.push(1)
s.push(2)
s.pop()
s.pop()
print(s.empty())

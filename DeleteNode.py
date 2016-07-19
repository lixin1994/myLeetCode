def deleteNode(node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node
        while temp != None:
            if temp.next != None:
                temp.val = temp.next.val

                if temp.next.next == None:
                    temp.next = None
                    break
                else:
                    temp = temp.next

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


a = ListNode(1)
b = ListNode(0)
b.next = a

deleteNode(b)

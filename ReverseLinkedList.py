class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None:
        return head
    start = None
    while head != None:
        temp = ListNode(head.val)
        temp.next = start
        start = temp
        head = head.next
    return start

a = ListNode(1)
b = ListNode(2)
a.next = b
reverseList(a );
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None:
        return None
    if head.next == None:
        return head
    temp = head.next
    while head != None and head.next != None:
        nxt = head.next
        head.next = nxt.next
        nxt.next = head
        new = head.next
        if head.next != None and head.next.next != None:
            head.next = head.next.next
        head = new
    return temp

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next=b
b.next=c
c.next=d
g = swapPairs(a)

while g:
    print(g.val)
    g = g.next
s = '123123'
print(list(s))

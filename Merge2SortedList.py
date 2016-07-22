class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    def cont(cur, l1 ,l2):
        if l1 is None:
            cur.next = l2
            return
        if l2 is None:
            cur.next = l1
            return
        if l1.val <= l2.val:
            cur.next = l1
            cont(cur.next, l1.next, l2)
        else:
            cur.next = l2
            cont(cur.next, l1, l2.next)
    head = ListNode(0)
    cur = head
    cont(cur, l1, l2)
    return head.next




a = ListNode(2)
b = ListNode(1)
c = ListNode(3)
d = ListNode(4)

# a.next = c
# b.next = d

g = mergeTwoLists(a, b)
while g:
    print(g.val)
    g = g.next
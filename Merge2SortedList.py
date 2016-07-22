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
    if l1 == None:
        return l2
    elif l2 == None:
        return l1
    result = l2
    bef = None
    while l1 != None:

        if l1.val <= l2.val and bef == None:
            nxt = l1.next
            l1.next = l2
            result = l1
            bef = l1
            l1 = nxt
        elif l1.val > l2.val and bef == None:
            bef = l2
        elif bef.val <= l1.val and l2 == None:
            bef.next = l1
            break
        elif bef.val <= l1.val <= l2.val:
            nxt = l1.next
            bef.next = l1
            l1.next = l2
            bef = l1
            l1 = nxt
        else:
            l2 = l2.next
            bef = bef.next
    return result

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
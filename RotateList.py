def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
        return head
    pointer1 = head
    pointer2 = head
    length = 0
    for i in range(0, k):
        pointer1 = pointer1.next
        if pointer1 == None:
            length = i + 1
            pointer1 = head
            break
    if k > length:
        k = k % length
        for i in range(0, k):
            pointer1 = pointer1.next
    while pointer1.next != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    result = pointer2.next
    pointer1.next = head
    pointer2.next = None
    return result

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c
res = rotateRight(a, 2000000)

while res:
    print(res.val)
    res = res.next
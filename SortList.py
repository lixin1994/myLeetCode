def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dic = []
    while head:
        dic.append((head.val,head))
        head = head.next
    sortedDic=sorted(dic,key=lambda t:t[0])
    for i, ele in enumerate(sortedDic):
        if i == len(sortedDic) - 1:
            ele[1].next == None
        else:
            ele[1].next = sortedDic[i + 1][1]
    return sortedDic[0][1]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = l = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l = l.next
                l1 = l1.next
            else:
                l.next = l2
                l = l.next
                l2 = l2.next
        l.next = l1 if l1 else l2
        return h.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l = Solution().mergeTwoLists(l1, l2)
while l:
    print(l.val)
    l = l.next

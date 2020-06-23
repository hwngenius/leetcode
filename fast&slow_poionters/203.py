class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        h = l = ListNode(0)
        while head:
            t=head.next
            if head.val != val:
                l.next = head
                l = head
                l.next=None
            head = t

        return h.next


l1 = ListNode(5)
l1.next = ListNode(6)
l1.next.next = ListNode(1)
l1.next.next.next = ListNode(6)
l = Solution().removeElements(l1, 6)
while l:
    print(l.val)
    l = l.next

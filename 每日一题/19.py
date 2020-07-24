class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        h = ListNode(0)
        h.next=head
        slow = fast=h
        while n > 0:
            fast = fast.next
            n -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return h.next


h = l = ListNode(0)
for i in range(1, 6):
    l.next = ListNode(i)
    l = l.next
l = Solution().removeNthFromEnd(h.next, 1)
while l:
    print(l.val)
    l = l.next

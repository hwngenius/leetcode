class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        t1 = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(t1)
        h = l = ListNode(0)
        while left and right:
            if left.val < right.val:
                l.next = left
                left = left.next
            else:
                l.next = right
                right = right.next
            l=l.next
        if right:
            l.next=right
        else:
            l.next=left
        return h.next


head=ListNode(4)
head.next=ListNode(2)
head.next.next=ListNode(1)
head.next.next.next=ListNode(3)
l=Solution().sortList(head)
while l:
    print(l.val)
    l=l.next
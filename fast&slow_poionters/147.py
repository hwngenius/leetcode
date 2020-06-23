class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None: return None
        h = ListNode(0)
        h.next = head
        head_front, head = head, head.next
        while head:
            h1, h2 = h, h.next
            while h2 and h2.val < head.val:
                h1, h2 = h2, h2.next
            if h2==head or h2 is None:
                h1.next = head
                head_front=head
                head = head.next
                head_front.next=None
            else:
                t = head.next
                head.next = h2
                h1.next = head
                head_front.next = None
                head = t
        return h.next


l1 = ListNode(-1)
l1.next = ListNode(5)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next=ListNode(0)
l = Solution().insertionSortList(l1)
while l:
    print(l.val)
    l = l.next

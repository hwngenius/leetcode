class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = l = ListNode(0)
        l.next = head
        l = l.next
        while head:
            while head and head.val == l.val:
                head = head.next
            l.next = head
            l = l.next
            if head:
                head = head.next
        return h.next


head = ListNode(1)
# head.next = ListNode(1)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(2)
l = Solution().deleteDuplicates(head)
while l:
    print(l.val)
    l = l.next

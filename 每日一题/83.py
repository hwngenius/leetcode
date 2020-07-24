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
            l = head

        return h.next


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)

print(Solution().deleteDuplicates(head))

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        right = head
        h = left = ListNode(0)
        while right:
            if right.next and right.val == right.next.val:
                t_val = right.val
                while right and right.val == t_val:
                    right = right.next
            else:
                left.next = right
                left = left.next
                right = right.next
                left.next = None

        return h.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
# head.next.next.next=ListNode(3)
# head.next.next.next.next=ListNode(4)
# head.next.next.next.next.next=ListNode(4)
# head.next.next.next.next.next.next=ListNode(5)

h = Solution().deleteDuplicates(head=head)
while h:
    print(h.val)
    h = h.next

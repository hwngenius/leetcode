class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        data = {}
        index = 0
        while head:
            if head not in data:
                data[head] = index
                index += 1
                head = head.next
            else:
                return head
        return None


head = ListNode(1)
head.next = ListNode(2)
l = Solution().detectCycle(head)
print(l)

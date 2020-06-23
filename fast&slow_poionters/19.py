class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l=ListNode(0)
        l.next=head
        fast=l
        while n>0:
            fast=fast.next
            n-=1
        slow=l
        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return l.next


head = ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
n = 3

l = Solution().removeNthFromEnd(head, n)
while l:
    print(l.val)
    l=l.next
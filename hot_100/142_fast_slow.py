class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow,fast=head,head
        while fast:
            slow=slow.next
            if fast.next:
                fast=fast.next.next
            else:
                return None
            if fast==slow:
                while head!=slow:
                    slow=slow.next
                    head=head.next
                return head
        return None

# 
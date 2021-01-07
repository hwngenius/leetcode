class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast=head
        while n>0:
            fast=fast.next
            n-=1
        slow=head
        if not fast:
            return head.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head

# 执行用时：
# 32 ms
# , 在所有 Python3 提交中击败了
# 97.17%
# 的用户
# 内存消耗：
# 14.8 MB
# , 在所有 Python3 提交中击败了
# 7.18%
# 的用户
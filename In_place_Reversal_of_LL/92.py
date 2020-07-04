class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        ans=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return ans
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n:
            return head
        fast, slow = head, head
        slow_pre=ListNode(float('inf'))
        counter_m=m
        while counter_m>1:
            slow_pre=slow
            slow=slow.next
            counter_m-=1
        while n>1:
            fast=fast.next
            n-=1

        later_link=fast.next
        fast.next=None
        slow_pre.next=self.reverseList(slow)
        slow.next=later_link
        if m==1:
            return slow_pre.next
        else:
            return head

# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 74.63%
# 的用户
# 内存消耗：
# 13.9 MB
# , 在所有 Python3 提交中击败了
# 25.00%
# 的用户
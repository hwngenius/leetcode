# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        slow,fast=head,head.next
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
        fast,slow.next=slow.next,None
        left,right=self.sortList(head),self.sortList(fast)
        ans=l=ListNode(0)
        while left and right:
            if left.val<right.val:l.next,left=left,left.next
            else:l.next,right=right,right.next
            l=l.next
        l.next=right if right else left
        return ans.next


# 执行用时：
# 432 ms
# , 在所有 Python3 提交中击败了
# 36.13%
# 的用户
# 内存消耗：
# 29.9 MB
# , 在所有 Python3 提交中击败了
# 15.57%
# 的用户
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        t=ans=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                t.next=l1
                l1=l1.next
            else:
                t.next=l2
                l2=l2.next
            t=t.next
        if l1:
            t.next=l1
        else:
            t.next=l2
        return ans.next


# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 73.97%
# 的用户
# 内存消耗：
# 14.8 MB
# , 在所有 Python3 提交中击败了
# 8.69%
# 的用户
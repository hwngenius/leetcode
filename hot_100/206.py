# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head
        a,b=head,head.next
        while b:
            c=b.next
            b.next=a
            a,b=b,c
        head.next=None
        return a


# 执行用时：
# 52 ms
# , 在所有 Python3 提交中击败了
# 17.01%
# 的用户
# 内存消耗：
# 15.5 MB
# , 在所有 Python3 提交中击败了
# 29.56%
# 的用户
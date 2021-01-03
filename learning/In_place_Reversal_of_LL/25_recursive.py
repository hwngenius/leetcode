# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_one(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ans = self.reverse_one(head.next)
        head.next.next = head
        head.next = None
        return ans

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l = head
        count = k
        while l and count > 1:
            l = l.next
            count -= 1
        if l is None:
            return head
        next_link=self.reverseKGroup(l.next,k)
        l.next=None
        ans=self.reverse_one(head)
        head.next=next_link
        return ans


# 执行用时：
# 52 ms
# , 在所有 Python3 提交中击败了
# 86.56%
# 的用户
# 内存消耗：
# 15 MB
# , 在所有 Python3 提交中击败了
# 7.69%
# 的用户

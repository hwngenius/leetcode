class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        t=head.next
        next_link=self.swapPairs(t.next)
        head.next=next_link
        t.next=head
        return t


# 执行用时：
# 36 ms
# , 在所有 Python3 提交中击败了
# 90.08%
# 的用户
# 内存消耗：
# 13.6 MB
# , 在所有 Python3 提交中击败了
# 6.25%
# 的用户

#
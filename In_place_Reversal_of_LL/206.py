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


# 执行用时：
# 56 ms
# , 在所有 Python3 提交中击败了
# 18.41%
# 的用户
# 内存消耗：
# 18.3 MB
# , 在所有 Python3 提交中击败了
# 5.88%
# 的用户
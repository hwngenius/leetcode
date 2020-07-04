class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast=head
        while fast and fast.next:
            head=head.next
            fast=fast.next.next

        return head


# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 67.04%
# 的用户
# 内存消耗：
# 13.8 MB
# , 在所有 Python3 提交中击败了
# 14.29%
# 的用户
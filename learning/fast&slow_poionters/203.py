class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        h = l = ListNode(0)
        while head:
            if head.val != val:
                l.next = head
                l = l.next
            head = head.next
        l.next=head
        return h.next

# 执行用时：
# 76 ms
# , 在所有 Python3 提交中击败了
# 75.41%
# 的用户
# 内存消耗：
# 16.8 MB
# , 在所有 Python3 提交中击败了
# 11.11%
# 的用户

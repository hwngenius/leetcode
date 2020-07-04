class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = l = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l = l.next
                l1 = l1.next
            else:
                l.next = l2
                l = l.next
                l2 = l2.next
        l.next = l1 if l1 else l2
        return h.next


# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 80.12%
# 的用户
# 内存消耗：
# 13.4 MB
# , 在所有 Python3 提交中击败了
# 7.14%
# 的用户

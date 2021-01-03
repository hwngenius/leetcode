class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode):
        if head:
            slow, fast = head, head.next
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            stack = []
            fast = slow.next
            slow.next = None
            while fast:
                stack.append(fast)
                fast = fast.next
            l = head.next
            h = head
            while l and len(stack) != 0:
                t = stack.pop()
                t.next = l
                head.next = t
                head = l
                l = l.next
            if l:
                head.next = l
            if len(stack):
                head.next = stack.pop()
            head=head.next
            if head:
                head.next=None
        #     return h
        # return None

# 执行用时：
# 92 ms
# , 在所有 Python3 提交中击败了
# 92.40%
# 的用户
# 内存消耗：
# 23.1 MB
# , 在所有 Python3 提交中击败了
# 20.00%
# 的用户
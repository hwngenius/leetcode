class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not (head and head.next):
            return True

        def reserve(head: ListNode) -> ListNode:
            if head:
                head_next = head.next
                head.next = None
                while head_next:
                    t = head_next.next
                    head_next.next = head
                    head = head_next
                    head_next = t
            return head

        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            l2 = slow.next.next
        else:
            l2 = slow.next
        slow.next = None
        l1 = reserve(head)
        while l1 and l2 and l1.val == l2.val:
            l1 = l1.next
            l2 = l2.next
        if l1 or l2:
            return False
        return True


# 执行用时：
# 128 ms
# , 在所有 Python3 提交中击败了
# 8.53%
# 的用户
# 内存消耗：
# 23.7 MB
# , 在所有 Python3 提交中击败了
# 25.00%
# 的用户
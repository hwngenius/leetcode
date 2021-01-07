class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# 执行用时：
# 80 ms
# , 在所有 Python3 提交中击败了
# 10.74%
# 的用户
# 内存消耗：
# 17.8 MB
# , 在所有 Python3 提交中击败了
# 5.14%
# 的用户
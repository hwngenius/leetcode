class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer=head
        def recursive(node=head)->bool:
            if node:
                if not recursive(node.next):
                    return False
                if self.front_pointer.val!=node.val:
                    return False
                self.front_pointer=self.front_pointer.next
                return True
            return True
        return recursive()

# 执行用时：
# 112 ms
# , 在所有 Python3 提交中击败了
# 15.65%
# 的用户
# 内存消耗：
# 76 MB
# , 在所有 Python3 提交中击败了
# 5.00%
# 的用户
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n==0:
            return None
        root_index = n // 2
        root = TreeNode(nums[root_index])
        root.left = self.sortedArrayToBST(nums[:root_index])
        root.right = self.sortedArrayToBST(nums[root_index + 1:])
        return root



# 执行用时：
# 72 ms
# , 在所有 Python3 提交中击败了
# 19.05%
# 的用户
# 内存消耗：
# 15.9 MB
# , 在所有 Python3 提交中击败了
# 9.52%
# 的用户
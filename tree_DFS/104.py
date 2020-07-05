class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))


# 执行用时：
# 68 ms
# , 在所有 Python3 提交中击败了
# 13.79%
# 的用户
# 内存消耗：
# 15.7 MB
# , 在所有 Python3 提交中击败了
# 5.55%
# 的用户

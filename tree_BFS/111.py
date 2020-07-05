class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None:
            return 1+self.minDepth(root.right)
        if root.right is None:
            return 1+self.minDepth(root.left)
        return 1+min(self.minDepth(root.left), self.minDepth(root.right))


# 执行用时：
# 64 ms
# , 在所有 Python3 提交中击败了
# 30.51%
# 的用户
# 内存消耗：
# 15.4 MB
# , 在所有 Python3 提交中击败了
# 12.50%
# 的用户

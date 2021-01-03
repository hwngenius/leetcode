class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.right, root.left = self.invertTree(
                root.left), self.invertTree(root.right)
        return root


# 执行用时：
# 36 ms
# , 在所有 Python3 提交中击败了
# 88.10%
# 的用户
# 内存消耗：
# 13.8 MB
# , 在所有 Python3 提交中击败了
# 5.26%
# 的用户

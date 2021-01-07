# class TreeNode:
def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            left=root.left
            root.left=self.invertTree(root.right)
            root.right=self.invertTree(left)
        return root


# 执行用时：
# 24 ms
# , 在所有 Python3 提交中击败了
# 99.59%
# 的用户
# 内存消耗：
# 14.8 MB
# , 在所有 Python3 提交中击败了
# 8.95%
# 的用户
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        def myfun(root: TreeNode, total: int) -> bool:
            if root.left is None and root.right is None:
                return sum == total+root.val
            if root.left is None:
                return myfun(root.right, total+root.val)
            if root.right is None:
                return myfun(root.left, total+root.val)
            return myfun(root.right, total+root.val) or myfun(root.left, total+root.val)
        return myfun(root, 0)


# 执行用时：
# 48 ms
# , 在所有 Python3 提交中击败了
# 92.95%
# 的用户
# 内存消耗：
# 15.5 MB
# , 在所有 Python3 提交中击败了
# 6.67%
# 的用户

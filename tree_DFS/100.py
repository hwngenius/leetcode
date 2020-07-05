class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


# 执行用时：
# 36 ms
# , 在所有 Python3 提交中击败了
# 88.36%
# 的用户
# 内存消耗：
# 13.6 MB
# , 在所有 Python3 提交中击败了
# 7.14%
# 的用户

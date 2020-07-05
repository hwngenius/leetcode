class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        if root is None:
            return self.ans

        def myfun(root: TreeNode) -> int:
            if root is None:
                return 0
            left_child = myfun(root.left)
            right_child = myfun(root.right)
            res_t = root.val
            if left_child > 0:
                res_t += left_child
            if right_child > 0:
                res_t += right_child
            self.ans = max(self.ans, res_t)
            if left_child <= 0 and right_child <= 0:
                return root.val
            return root.val+max(left_child, right_child)
        myfun(root)
        return self.ans


# 执行用时：
# 104 ms
# , 在所有 Python3 提交中击败了
# 78.27%
# 的用户
# 内存消耗：
# 21.1 MB
# , 在所有 Python3 提交中击败了
# 20.00%
# 的用户

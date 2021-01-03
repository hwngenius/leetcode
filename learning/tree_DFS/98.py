class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        res = []

        def midTravel(root: TreeNode):
            if root:
                midTravel(root.left)
                res.append(root.val)
                midTravel(root.right)
        midTravel(root)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True


# 执行用时：
# 52 ms
# , 在所有 Python3 提交中击败了
# 88.62%
# 的用户
# 内存消耗：
# 16.9 MB
# , 在所有 Python3 提交中击败了
# 9.52%
# 的用户

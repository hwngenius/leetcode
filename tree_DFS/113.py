from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        path = []
        from copy import deepcopy

        def myfun(root: TreeNode, total: int = 0):
            path.append(root.val)
            if root.left is None and root.right is None:
                if total+root.val == sum:
                    ans.append(deepcopy(path))
            else:
                if root.left is None:
                    myfun(root.right, total+root.val)
                elif root.right is None:
                    myfun(root.left, root.val+total)
                else:
                    myfun(root.left, total+root.val)
                    myfun(root.right, root.val+total)
            path.pop()
        myfun(root)
        return ans


# 执行用时：
# 64 ms
# , 在所有 Python3 提交中击败了
# 26.33%
# 的用户
# 内存消耗：
# 15.1 MB
# , 在所有 Python3 提交中击败了
# 22.22%
# 的用户

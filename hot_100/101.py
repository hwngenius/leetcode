# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def myfun(node1:TreeNode,node2:TreeNode)->bool:
            if node1 and node2:
                if node1.val!=node2.val:
                    return False
                return myfun(node1.left,node2.right) and myfun(node1.right,node2.left)

            if not node1 and not node2:
                return True
        if not root:return True
        return myfun(root.left,root.right)


# 执行用时：
# 52 ms
# , 在所有 Python3 提交中击败了
# 15.45%
# 的用户
# 内存消耗：
# 14.9 MB
# , 在所有 Python3 提交中击败了
# 13.73%
# 的用户
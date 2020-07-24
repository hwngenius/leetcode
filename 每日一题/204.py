class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def my_fun(root:TreeNode)->int:
            if root is None:return 0
            left_height,right_height=my_fun(root.left),my_fun(root.right)
            return 1+min(left_height,right_height)
        return my_fun(root)
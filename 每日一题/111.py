class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def my_fun(root:TreeNode)->int:
            if root is None:return 0
            if root.left and root.right:return 1+min(my_fun(root.left),my_fun(root.right))
            if root.left and not root.right:return 1+my_fun(root.left)
            if root.right and not root.left:return 1+my_fun(root.right)
            else: return 1
        return my_fun(root)
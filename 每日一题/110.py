class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def my_fun(root:TreeNode)->(bool,int):
            if root is None:
                return True,0
            left_flag,left_height=my_fun(root.left)
            right_flag,right_height=my_fun(root.right)
            if not (left_flag and right_flag) or (abs(right_height-left_height)>1):return False, -1
            return True,1+max(right_height,left_height)
        return my_fun(root)[0]


root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(2)
root.left.left=TreeNode(3)
root.left.right=TreeNode(3)
root.left.left.left=TreeNode(4)
root.left.left.right=TreeNode(4)

print(Solution().isBalanced(root))
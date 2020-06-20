# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def height(self,root:TreeNode)->(int,bool):
        if root is None:
            return (0,True)
        left_height,left_balance=self.height(root.left)
        if left_balance is not True:
            return (-1,False)
        right_height,right_balance=self.height(root.right)
        if right_balance is not True:
            return (-1,False)
        else:
            return 1+max(left_height,right_height),abs(left_height-right_height)<=1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root)[1]

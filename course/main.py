class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        global ans
        if root is None:
            return ans
        def myfun(root:TreeNode)->int:
            global ans
            if root is None:
                return 0
            left_child=myfun(root.left)
            right_child=myfun(root.right)
            res=root.val
            if left_child>0:
                res+=left_child
            if right_child>0:
                res+=right_child
            ans=max(ans,res)
            return res
        myfun(root)
        return ans
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        def my_fun(root:TreeNode):
            if root is not None:
                ans.append(root.val)
                my_fun(root.left)
                my_fun(root.right)
        my_fun(root)
        return ans
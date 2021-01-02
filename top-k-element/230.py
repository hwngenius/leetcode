# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans=0
        self.count=0
        def myfun(root:TreeNode):
            if root is not None and self.count<k:
                myfun(root.left)
                self.count+=1
                if self.count==k:
                    self.ans=root.val
                myfun(root.right)
        myfun(root)
        return self.ans

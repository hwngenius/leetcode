# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val=root.val
        left_val=p.val
        right_val=q.val
        if parent_val>left_val and parent_val>right_val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif parent_val<left_val and parent_val<right_val:
            return self.lowestCommonAncestor(root.right,q,p)
        return root
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p and q:
            return q.val == p.val and self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        return False

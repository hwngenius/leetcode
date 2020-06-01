# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        u,v=root,root
        queue= [u, v]
        while queue:
            u, v = queue[0], queue[1]
            queue=queue[2:]
            if u is None and v is None:
                return True
            if u is None or v is None:
                return False
            if u.val!=v.val:
                return False
            queue.append(u.left)
            queue.append(v.right)
            queue.append(u.right)
            queue.append(v.left)
        return True


root=TreeNode(9)
root.left=TreeNode(-42)
root.right=TreeNode(-42)
root.left.right=TreeNode(76)
root.right.left=TreeNode(76)
root.left.right.left=TreeNode(13)
root.right.left.left=TreeNode(13)

print(Solution().isSymmetric(root))
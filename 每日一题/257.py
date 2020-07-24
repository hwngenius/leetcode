from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if not root.right and not root.left:
            return [str(root.val)]
        sub_path=self.binaryTreePaths(root.left)+self.binaryTreePaths(root.right)
        return [str(root.val)+'->'+c for c in sub_path] 
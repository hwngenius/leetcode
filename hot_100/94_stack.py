from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        ans=[]
        while root or len(stack)>0:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            ans.append(root.val)
            root=root.right
        return ans

root=TreeNode(1)
root.right=TreeNode(2)
root.right.left=TreeNode(3)
print(Solution().inorderTraversal(root))
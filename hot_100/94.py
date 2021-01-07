# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        def myfun(root:TreeNode):
            if root:
                myfun(root.left)
                ans.append(root.val)
                myfun(root.right)
        myfun(root)
        return ans

# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 58.22%
# 的用户
# 内存消耗：
# 14.8 MB
# , 在所有 Python3 提交中击败了
# 5.07%
# 的用户
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        level=[]
        ans=0
        level.append(root)
        while level:
            n=len(level)
            ans+=1
            for i in range(n):
                node=level[i]
                if node.left:level.append(node.left)
                if node.right:level.append(node.right)
            level=level[n:]
        return ans

# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 89.33%
# 的用户
# 内存消耗：
# 15.8 MB
# , 在所有 Python3 提交中击败了
# 21.61%
# 的用户
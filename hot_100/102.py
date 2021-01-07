# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        ans=[]
        level=[]
        level.append(root)
        while level:
            t=[]
            n=len(level)
            for i in range(n):
                node=level[i]
                t.append(node.val)
                if node.left:level.append(node.left)
                if node.right:level.append(node.right)
            level=level[n:]
            ans.append(t[:])
        return ans


# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 72.16%
# 的用户
# 内存消耗：
# 15.2 MB
# , 在所有 Python3 提交中击败了
# 10.98%
# 的用户
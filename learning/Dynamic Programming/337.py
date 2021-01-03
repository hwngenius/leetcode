# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        val=self.dfs(root)
        return max(val[0],val[1])
    def dfs(self,root:TreeNode)->List[int]:
        if not root:
            return [0,0]
        l,r=self.dfs(root.left),self.dfs(root.right)
        selected=root.val+l[1]+r[1]
        not_selected=max(l[0],l[1])+max(r[0],r[1])
        return [selected,not_selected]

# 执行用时：
# 60 ms
# , 在所有 Python3 提交中击败了
# 61.49%
# 的用户
# 内存消耗：
# 16.6 MB
# , 在所有 Python3 提交中击败了
# 31.73%
# 的用户
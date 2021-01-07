# Definition for a binary tree node.

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:return None
        root=TreeNode(preorder[0])
        boader=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:boader+1],inorder[:boader])
        root.right=self.buildTree(preorder[boader+1:],inorder[boader+1:])
        return root


# 执行用时：
# 212 ms
# , 在所有 Python3 提交中击败了
# 23.80%
# 的用户
# 内存消耗：
# 86.8 MB
# , 在所有 Python3 提交中击败了
# 16.63%
# 的用户
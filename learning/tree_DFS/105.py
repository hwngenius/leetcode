from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        left_num = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:left_num+1], inorder[:left_num])
        root.right = self.buildTree(
            preorder[left_num+1:], inorder[left_num+1:])
        return root


# 执行用时：
# 188 ms
# , 在所有 Python3 提交中击败了
# 62.39%
# 的用户
# 内存消耗：
# 87.6 MB
# , 在所有 Python3 提交中击败了
# 11.11%
# 的用户

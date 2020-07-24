from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        else:
            root = TreeNode(preorder[0])
            left_num = inorder.index(preorder[0])
            root.left = self.buildTree(preorder[1:1 + left_num], inorder[:left_num])
            root.right = self.buildTree(preorder[1 + left_num:], inorder[left_num + 1:])
            return root

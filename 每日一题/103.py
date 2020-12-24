# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        tmp,stack,res,flag=[],[root],[],1
        while stack:
            for _ in range(len(stack)):
                node=stack.pop(0)
                tmp.append(node.val)
                if node.left:stack.append(node.left)
                if node.right:stack.append(node.right)
            res.append(tmp[::flag])
            flag*=-1
            tmp=[]
        return res
        

# 执行用时：
# 32 ms
# , 在所有 Python3 提交中击败了
# 96.87%
# 的用户
# 内存消耗：
# 14.9 MB
# , 在所有 Python3 提交中击败了
# 5.03%
# 的用户
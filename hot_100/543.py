class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans=0
        def max_length(root:TreeNode)->int:
            if root:
                left=max_length(root.left)
                right=max_length(root.right)
                self.ans=max(self.ans,left+right)
                return 1+max(left,right)
            return 0
        if not root:return 0
        max_length(root)
        return self.ans

# 执行用时：
# 56 ms
# , 在所有 Python3 提交中击败了
# 54.01%
# 的用户
# 内存消耗：
# 16.9 MB
# , 在所有 Python3 提交中击败了
# 13.60%
# 的用户

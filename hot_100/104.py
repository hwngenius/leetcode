class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def my_fun(root:TreeNode)->int:
            if root is None:return 0
            left_height,right_height=my_fun(root.left),my_fun(root.right)
            return 1+max(left_height,right_height)
        return my_fun(root)

# 执行用时：
# 56 ms
# , 在所有 Python3 提交中击败了
# 30.13%
# 的用户
# 内存消耗：
# 16.8 MB
# , 在所有 Python3 提交中击败了
# 5.20%
# 的用户
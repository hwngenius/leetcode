class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nums=[]
        stack=[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            nums.append(root.val)
            root=root.right
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                return False
        return True


# 执行用时：
# 64 ms
# , 在所有 Python3 提交中击败了
# 17.69%
# 的用户
# 内存消耗：
# 17 MB
# , 在所有 Python3 提交中击败了
# 17.61%
# 的用户
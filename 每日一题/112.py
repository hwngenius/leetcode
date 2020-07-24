class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def myfun(root: TreeNode, last_sum: int) -> bool:

            if root is None: return False
            # print(last_sum, root.val, root.val + last_sum)
            if root.left is None and root.right is None and last_sum + root.val == sum:
                return True
            else:
                return myfun(root.left, last_sum + root.val) or myfun(root.right,
                                                                                          last_sum + root.val)

        return myfun(root, 0)


root=TreeNode(5)
root.left=TreeNode(4)
root.left.left=TreeNode(11)
root.left.left.right=TreeNode(2)

print(Solution().hasPathSum(root,22))
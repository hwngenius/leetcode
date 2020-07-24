from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([])
        next_num = 1
        ans = []
        queue.append(root)
        while queue:
            level = []
            current_num = next_num
            next_num = 0
            while current_num > 0:
                current_num -= 1
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    next_num += 1
                    queue.append(node.left)
                if node.right:
                    next_num += 1
                    queue.append(node.right)
            ans.append(level)
        return ans


root=TreeNode(3)
root.left=TreeNode(9)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)
print(Solution().levelOrder(root))
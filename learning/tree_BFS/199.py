from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        from collections import deque
        ans = []
        if root is None:
            return ans
        queue = deque([root])
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if i == length-1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 80.96%
# 的用户
# 内存消耗：
# 13.8 MB
# , 在所有 Python3 提交中击败了
# 14.29%
# 的用户

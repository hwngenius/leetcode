from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        from collections import deque
        if root is None:
            return [0]
        ans = []
        queue = deque([root])
        while queue:
            level_sum, length = 0, len(queue)
            for _ in range(length):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level_sum/length)
        return ans


# 执行用时：
# 84 ms
# , 在所有 Python3 提交中击败了
# 17.75%
# 的用户
# 内存消耗：
# 16 MB
# , 在所有 Python3 提交中击败了
# 16.67%
# 的用户

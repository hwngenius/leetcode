from typing import List
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = collections.deque([root])
        ans = []
        counter = 0
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if counter % 2 == 0:
                ans.append(level)
            else:
                ans.append(level[::-1])
            counter += 1
        return ans


# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 57.56%
# 的用户
# 内存消耗：
# 13.9 MB
# , 在所有 Python3 提交中击败了
# 5.55%
# 的用户

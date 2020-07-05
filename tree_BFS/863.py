from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if root is None:
            return []

        def bfs(root: TreeNode, parent: int = None):
            if root is not None:
                root.par = parent
                bfs(root.left, root)
                bfs(root.right, root)
        bfs(root)

        seen = {target}
        from collections import deque
        queue = deque([(target, 0)])
        while queue:
            if queue[0][1] == K:
                return [node.val for node, _ in queue]
            node, d = queue.popleft()
            seen.add(node)
            if node.left and node.left not in seen:
                queue.append((node.left, d+1))
            if node.right and node.right not in seen:
                queue.append((node.right, d+1))
            if node.part and node.par not in seen:
                queue.append((node.par, d+1))
        return []


# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 93.47%
# 的用户
# 内存消耗：
# 14 MB
# , 在所有 Python3 提交中击败了
# 100.00%
# 的用户

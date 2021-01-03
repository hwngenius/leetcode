class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        from collections import deque
        queue = deque([root])
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if i != length-1:
                    node.next = queue[0]
                else:
                    node.next = None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


# 执行用时：
# 104 ms
# , 在所有 Python3 提交中击败了
# 16.74%
# 的用户
# 内存消耗：
# 15.2 MB
# , 在所有 Python3 提交中击败了
# 20.00%
# 的用户

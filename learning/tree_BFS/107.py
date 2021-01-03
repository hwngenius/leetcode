class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:return []
        from collections import deque
        queue=deque([root])
        ans=[]

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        ans.reverse()
        return ans

# 执行用时：
# 48 ms
# , 在所有 Python3 提交中击败了
# 38.23%
# 的用户
# 内存消耗：
# 14.1 MB
# , 在所有 Python3 提交中击败了
# 6.25%
# 的用户
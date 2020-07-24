from typing import List


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        row, col = len(A), len(A[0])

        def neibor(i, j):
            for r, c in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                if 0 <= r < row and 0 <= c < col:
                    yield r, c

        def find_island():
            for i in range(row):
                for j in range(col):
                    if A[i][j] == 1:
                        return i, j

        vis = [[False for _ in range(col)] for _ in range(row)]
        from collections import deque
        queue = deque([])

        def travel(i, j):
            if vis[i][j] == False and A[i][j] == 1:
                queue.append((i, j, 0))
                vis[i][j] = True
                for r, c in neibor(i, j):
                    travel(r, c)

        i, j = find_island()
        travel(i, j)
        while deque:
            i, j, cost = queue.popleft()
            for r, c in neibor(i, j):
                if vis[r][c] is False:
                    if A[r][c] == 1:
                        return cost
                    else:
                        vis[r][c] = True
                        queue.append((r, c, cost + 1))

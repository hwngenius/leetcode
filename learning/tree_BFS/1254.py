from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        if row == 1 or col == 1:
            return 0

        def neibor(i, j):
            connect = [
                (i+1, j), (i-1, j),
                (i, j-1), (i, j+1)
            ]
            for r, c in connect:
                if 0 <= r < row and 0 <= c < col:
                    yield r, c
        ans = 0
        vis = [[False for _ in range(col)]for _ in range(row)]

        def travel(i, j):
            if vis[i][j] == False and grid[i][j] == 0:
                vis[i][j] = True
                for r, c in neibor(i, j):
                    travel(r, c)
        i1, i2 = 0, row-1
        for j in range(col):
            travel(i1, j)
            travel(i2, j)
        j1, j2 = 0, col-1
        for i in range(row):
            travel(i, j1)
            travel(i, j2)
        for i in range(1, row-1):
            for j in range(1, col-1):
                if vis[i][j] == False and grid[i][j] == 0:
                    ans += 1
                    travel(i, j)
        return ans


# 执行用时：
# 172 ms
# , 在所有 Python3 提交中击败了
# 46.54%
# 的用户
# 内存消耗：
# 14.5 MB
# , 在所有 Python3 提交中击败了
# 100.00%
# 的用户

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        for r in range(row - 2, -1, -1):
            for i in range(len(triangle[r])):
                triangle[r][i] += min(triangle[r + 1][i], triangle[r + 1][i + 1])
        return triangle[0][0]


print(Solution().minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))

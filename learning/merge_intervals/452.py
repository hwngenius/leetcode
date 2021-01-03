from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort()
        t = points[0]
        for i in range(1, len(points)):
            if t[1] >= points[i][0]:
                t[0] = max(points[i][0], t[0])
                t[1] = min(points[i][1], t[1])
            else:
                ans += 1
                t = points[i]
        return ans+1


# 执行用时：
# 608 ms
# , 在所有 Python3 提交中击败了
# 23.52%
# 的用户
# 内存消耗：
# 19 MB
# , 在所有 Python3 提交中击败了
# 33.33%
# 的用户
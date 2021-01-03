from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        ans = 0
        intervals.sort()
        t = intervals[0]
        index = 1
        while index < len(intervals):
            if intervals[index][0] < t[1]:
                ans += 1
                t[1] = min(t[1], intervals[index][1])
            else:
                t = intervals[index]
            index += 1
        return ans


# 执行用时：
# 80 ms
# , 在所有 Python3 提交中击败了
# 98.08%
# 的用户
# 内存消耗：
# 16.9 MB
# , 在所有 Python3 提交中击败了
# 100.00%
# 的用户
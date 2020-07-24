from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals
        ans = []
        ans.append(intervals[0])
        i = 1
        while i < len(intervals):
            if intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                if intervals[i][1] > ans[-1][1]:
                    ans[-1][1] = intervals[i][1]
            i += 1
        return ans

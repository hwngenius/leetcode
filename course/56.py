from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        index = 0
        while index < len(intervals):

            a = intervals[index]
            if index == len(intervals) - 1:
                ans.append(a)
                break
            for i in range(index + 1, len(intervals)):
                if intervals[i][0] <= a[1]:
                    if a[1] < intervals[i][1]:
                        a[1] = intervals[i][1]
                    if i == len(intervals) - 1:
                        ans.append(a)
                        index = len(intervals)
                        break
                else:
                    ans.append(a)
                    index = i
                    break
        return ans


input = [[1, 3], [2, 8], [8, 15], [15, 18]]
print(Solution().merge(input))

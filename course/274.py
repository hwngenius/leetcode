from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        t = len(citations)
        if t == 0:
            return 0
        citations.sort()
        for i in range(t):
            if citations[i] >= t - i:
                return t - i
        return 0



print(Solution().hIndex([3,0,6,1,5]))
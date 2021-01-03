from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t=set()
        for i in nums:
            if i in t:
                return i
            else:
                t.add(i)
        return -1
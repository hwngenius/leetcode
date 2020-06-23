from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()


L = [0, 1,2]
Solution().sortColors(L)
print(L)

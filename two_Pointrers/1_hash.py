from typing import List
from collections import Counter


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data_hash = Counter(nums)
        for i, x in enumerate(nums):
            tmp = target - x
            if tmp in data_hash and tmp != x:
                return [i, nums.index(tmp)]
            elif tmp == x and data_hash[x] >= 2:
                return [i, nums[i+1:].index(x) + i+1]


nums = [1,3, 3]
target = 6

print(Solution().twoSum(nums, target))

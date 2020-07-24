from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        if target<nums[0]:
            return 0
        for i,x in enumerate(nums):
            if x<target:
                continue
            else:
                return i
        return len(nums)
nums=[1,3,5,6]
target=0
print(Solution().searchInsert(nums,target))
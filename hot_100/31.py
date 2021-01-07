from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n>1:
            for i in range(n-1):
                if nums[i]>nums[i+1]:
                    break
            if i!=0:
                nums[i],nums[i+1]=nums[i+1],nums[i]
            else:
                nums[0],nums[-1]=nums[-1],nums[0]



nums=[1,1,5]
Solution().nextPermutation(nums)
print(nums)
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans=float('inf')
        total=0
        left,right=0,-1
        while left<len(nums):
            while total<s and right+1<len(nums):
                right+=1
                total+=nums[right]
            if total>=s:
                ans=min(ans,right-left+1)
            left+=1
            total-=nums[left-1]
        return ans if ans!=float('inf') else 0



nums = [2, 3, 1, 2, 4, 3]
s = 7
print(Solution().minSubArrayLen(s, nums))

from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack=[]
        l,r=len(nums),0
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>nums[i]:
                l=min(l,stack.pop())
            stack.append(i)
        
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<nums[i]:
                r=max(r,stack.pop())
            stack.append(i)
        if r-l>0:
            return r-l+1
        else:
            return 0

nums=[2, 6, 4, 8, 10, 9,1,15]
print(Solution().findUnsortedSubarray(nums))
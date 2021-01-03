from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l=10000000
        for i in range(len(nums)-1):
           if nums[i]>nums[i+1]:
               l=min(nums[i+1],l)
        r=-10000000
        for i in range(len(nums)-1,0,-1):
            if nums[i]<nums[i-1]:
                r=max(r,nums[i-1])
        
        li,lr=0,0
        for i in range(len(nums)):
            if nums[i]>l:
                li=i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<r:
                lr=i
                break
        if li==lr:return 0
        return lr-li+1


# 执行用时：
# 112 ms
# , 在所有 Python3 提交中击败了
# 54.56%
# 的用户
# 内存消耗：
# 15.4 MB
# , 在所有 Python3 提交中击败了
# 5.03%
# 的用户
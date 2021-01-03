from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        if nums[l]<=nums[r]:return nums[l]
        while l<=r:
            mid=(l+r)//2
            if nums[mid+1]<nums[mid]:return nums[mid+1]
            if nums[mid-1]>nums[mid]:return nums[mid]
            if nums[mid]>nums[0]:l=mid+1
            else: r=mid-1
        



# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 38.41%
# 的用户
# 内存消耗：
# 15.1 MB
# , 在所有 Python3 提交中击败了
# 5.10%
# 的用户
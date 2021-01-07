from typing import List

class Solution:
    def search(self,nums:List[int],target:int)->int:
        if not nums: return -1
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1


# 执行用时：
# 28 ms
# , 在所有 Python3 提交中击败了
# 98.90%
# 的用户
# 内存消耗：
# 15.1 MB
# , 在所有 Python3 提交中击败了
# 8.02%
# 的用户
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(array,i,j):
            while i<=j:
                mid=(i+j)//2
                if array[mid]==target:
                    return mid
                elif array[mid]<target:
                    i=mid+1
                else:
                    j=mid-1
            return -1
        left=right=binary_search(nums,0,len(nums)-1)
        t=right
        while t!=-1 and nums[t+1:]:
            t=binary_search(nums,t+1,len(nums))
            right=max(t,right)
        t=left
        while t!=-1 and nums[:t]:
            t=binary_search(nums,0,t-1)
            if t!=-1:
                left=min(t,left)
        return [left,right]
        
# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 69.56%
# 的用户
# 内存消耗：
# 15.4 MB
# , 在所有 Python3 提交中击败了
# 9.49%
# 的用户
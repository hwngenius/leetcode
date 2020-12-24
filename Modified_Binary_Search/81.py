from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:return True
            if nums[l]<nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    r=mid-1
                else:
                    l=l+1
            elif nums[mid]==nums[l]:
                l+=1
            elif nums[mid]<=nums[r]:
                if nums[mid]<=target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return False


# 执行结果：
# 通过
# 显示详情
# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 71.89%
# 的用户
# 内存消耗：
# 15.2 MB
# , 在所有 Python3 提交中击败了
# 5.19%
# 的用户
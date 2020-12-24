class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        # if r==2:return 1

        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[mid+1]:
                r=mid
            else:
                l=mid
            if r==l+1:
                if nums[l-1]<nums[l] and nums[l]>nums[l+1]:
                    return l
                else:
                    return r
        return l


# 执行结果：
# 通过
# 显示详情
# 执行用时：
# 28 ms
# , 在所有 Python3 提交中击败了
# 99.15%
# 的用户
# 内存消耗：
# 14.9 MB
# , 在所有 Python3 提交中击败了
# 5.20%
# 的用户
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:return -1
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:return mid
            if nums[mid]>target:r=mid-1
            if nums[mid]<target:l=mid+1
        return -1


# 执行结果：
# 通过
# 显示详情
# 执行用时：
# 260 ms
# , 在所有 Python3 提交中击败了
# 98.97%
# 的用户
# 内存消耗：
# 16 MB
# , 在所有 Python3 提交中击败了
# 5.16%
# 的用户
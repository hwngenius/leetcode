class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num=nums[0]
        for i in range(1,len(nums)):
            num^=nums[i]
        return num

# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 96.47%
# 的用户
# 内存消耗：
# 16.5 MB
# , 在所有 Python3 提交中击败了
# 8.25%
# 的用户
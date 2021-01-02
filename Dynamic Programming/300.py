class Solution:
    def lengthOfLIS(self,nums)->int:
        if len(nums)==0:return 0
        dp=[1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[j]+1,dp[i])
        return max(dp)


# 执行用时：
# 3484 ms
# , 在所有 Python3 提交中击败了
# 25.76%
# 的用户
# 内存消耗：
# 15 MB
# , 在所有 Python3 提交中击败了
# 12.98%
# 的用户
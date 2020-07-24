class Solution:
    def lengthOfLIS(self,nums)->int:
        if len(nums)==0:return 0
        dp=[1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[j]+1,dp[i])
        return max(dp)


print(Solution().lengthOfLIS([]))
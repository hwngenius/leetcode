from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        count=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
                        count[i]=count[j]
                    elif dp[i]==dp[j]+1:
                        count[i]+=count[j]
    
        longest=max(dp)
        return sum(c for i,c in enumerate(count) if dp[i]==longest)

# 执行用时：
# 1268 ms
# , 在所有 Python3 提交中击败了
# 24.14%
# 的用户
# 内存消耗：
# 15.1 MB
# , 在所有 Python3 提交中击败了
# 12.26%
# 的用户
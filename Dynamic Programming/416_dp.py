from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if n<2:return False
        total=sum(nums)
        target,rem=divmod(total,2)
        if max(nums)>target:return False
        if rem:return False
        
        dp=[[False for _ in range(target+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        dp[0][nums[0]]=True

        for i in range(1,n):
            v=nums[i]
            for j in range(1,1+target):
                if v>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=(dp[i-1][j] or dp[i-1][j-v])

        return dp[-1][-1]


# 执行用时：
# 1956 ms
# , 在所有 Python3 提交中击败了
# 40.67%
# 的用户
# 内存消耗：
# 30.6 MB
# , 在所有 Python3 提交中击败了
# 7.05%
# 的用户
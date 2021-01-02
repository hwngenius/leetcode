class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp=[[0 for _ in range(2001)]for _ in range(len(nums))]
        dp[0][nums[0]+1000]=1
        dp[0][-nums[0]+1000]+=1
        for i in range(1,len(nums)):
            for total in range(-1000,1001):
                if dp[i-1][total+1000]>0:
                   dp[i][total+nums[i]+1000]+=dp[i-1][total+1000]
                   dp[i][total-nums[i]+1000]+=dp[i-1][total+1000]
        return dp[-1][S+1000] if -1000<=S<=1000 else 0

# 执行用时：
# 796 ms
# , 在所有 Python3 提交中击败了
# 20.11%
# 的用户
# 内存消耗：
# 15.1 MB
# , 在所有 Python3 提交中击败了
# 22.23%
# 的用户
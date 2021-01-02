from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        dp=[1e6 for _ in range(amount+1)]
        for i in range(1,amount+1):
            if i in coins:
                dp[i]=1
                continue
            for coin in coins:
                t=i-coin
                if t>0 and dp[t]!=1e6:
                    dp[i]=min(dp[t]+1,dp[i])
        return dp[-1] if dp[-1]!=1e6 else -1

# 执行用时：
# 1484 ms
# , 在所有 Python3 提交中击败了
# 43.23%
# 的用户
# 内存消耗：
# 14.9 MB
# , 在所有 Python3 提交中击败了
# 30.58%
# 的用户
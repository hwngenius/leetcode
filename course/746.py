from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0 for _ in range(len(cost))]
        dp[0],dp[1]=cost[0],cost[1]
        for i in range(2,len(dp)):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        return min(dp[len(dp)-2:])


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(Solution().minCostClimbingStairs(cost))
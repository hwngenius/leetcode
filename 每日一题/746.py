from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2,len(cost)):
            cost[i]=min(cost[i-1],cost[i-2])+cost[i]
        return min(cost[-2:])


cost= [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(Solution().minCostClimbingStairs(cost))
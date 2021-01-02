from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:return 0
        for i in range(len(prices)-1,0,-1):
            prices[i]-=prices[i-1]
        for i in range(2,len(prices)):
            if prices[i-1]>0:
                prices[i]+=prices[i-1]
        ans=max(prices[1:])
        ans=max(0,ans)
        return ans

# 执行用时：
# 56 ms
# , 在所有 Python3 提交中击败了
# 29.96%
# 的用户
# 内存消耗：
# 15.4 MB
# , 在所有 Python3 提交中击败了
# 23.61%
# 的用户
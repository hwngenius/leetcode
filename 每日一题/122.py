class Solution:
    def maxProfit(self,prices:List[int])->int:
        ans=0
        for i in range(len(prices)-1):
            prices[i]=prices[i+1]-prices[i]
            if prices[i]>0:
                ans+=prices[i]

        return ans

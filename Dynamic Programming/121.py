class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=1e9
        ans=0
        for price in prices:
            min_price=min(min_price,price)
            ans=max(price-min_price,ans)
        return ans
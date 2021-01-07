class Solution:
    def numSquares(self, n: int) -> int:
        import math
        t=int(math.sqrt(n))
        hash_table=set([i**2 for i in range(t+1)])
        dp=[1e9]*(n+1)
        for i in range(n+1):
            if i in hash_table:
                dp[i]=1
            else:
                for square in hash_table:
                    t=i-square
                    if t>=0:
                        if dp[t]!=1e9:
                            dp[i]=min(dp[i],dp[t]+1)
        return dp[-1]
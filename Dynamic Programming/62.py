class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0]=1
        for i in range(n):
            dp[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]


# 执行用时：
# 32 ms
# , 在所有 Python3 提交中击败了
# 93.87%
# 的用户
# 内存消耗：
# 14.9 MB
# , 在所有 Python3 提交中击败了
# 5.10%
# 的用
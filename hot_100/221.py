from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:return 0
        row,col=len(matrix),len(matrix[0])
        dp=[[0 for _ in range(col)] for _ in range(row)]
        ans=0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=='1':
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                    ans=max(ans,dp[i][j]**2)
        return ans


# 执行用时：
# 140 ms
# , 在所有 Python3 提交中击败了
# 15.82%
# 的用户
# 内存消耗：
# 20.2 MB
# , 在所有 Python3 提交中击败了
# 11.86%
# 的用户
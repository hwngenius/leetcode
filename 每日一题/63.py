class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row,col=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[row-1][col-1]:
            return 0
        dp=[[0]*col]*row
        for i in range(row):
            if obstacleGrid[i][0]==1:
                break
            else:
                dp[i][0]=1
        for i in range(col):
            if obstacleGrid[0][i]==1:
                break
            else:
                dp[0][i]=1
        for i in range(1,row):
            for j in range(1,col):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[row-1][col-1]
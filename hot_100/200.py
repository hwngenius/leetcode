class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:return 0
        row,col=len(grid),len(grid[0])
        def neighbord(i,j):
            for r,c in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if 0<=r<row and 0<=c<col:
                    yield (r,c)
        def DFS(i,j):
            vis[i][j]=True
            for r,c in neighbord(i,j):
                if vis[r][c] is False and grid[r][c]=='1':
                    DFS(r,c)
        ans=0
        vis=[[False for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and vis[i][j] is False:
                    ans+=1
                    DFS(i,j)
        return ans

# 执行用时：
# 112 ms
# , 在所有 Python3 提交中击败了
# 13.32%
# 的用户
# 内存消耗：
# 19.8 MB
# , 在所有 Python3 提交中击败了
# 5.02%
# 的用户
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:return matrix
        row,col=len(matrix),len(matrix[0])
        direction=[(0,1),(1,0),(0,-1),(-1,0)]*max(row,col)
        ans=[]
        count=row*col
        vis=[[False for _ in range(col)] for _ in range(row)]
        idx=0
        index=[0,-1]
        for d in direction:
            if idx>=count:
                break
            while 0<=index[0]+d[0]<row and 0<=index[1]+d[1]<col and vis[index[0]+d[0]][index[1]+d[1]] is False:
                index[0]+=d[0]
                index[1]+=d[1]
                vis[index[0]][index[1]]=True
                ans.append(matrix[index[0]][index[1]])
                idx+=1
        
        return ans


# 执行用时：
# 32 ms
# , 在所有 Python3 提交中击败了
# 93.39%
# 的用户
# 内存消耗：
# 15 MB
# , 在所有 Python3 提交中击败了
# 5.02%
# 的用户
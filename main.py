import collections


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
       vis=[[False for _ in range(len(A))] for _ in range(len(A))]

       def neighbors(r, c):
          for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
             if 0 <= nr < R and 0 <= nc < C:
                yield nr, nc

       def travel(i,j):
          if vis[i][j] is not True:
             vis[i][j]=True
             for nexti,nextj in neighbors(i,j):
                travel(nexti,nextj)

       def findstart():
          for i in range(len(A)):
             for j in range(len(A)):
                if A[i][j]==1:
                   return i,j

       starti,startj=findstart()
       travel(starti,startj)
       vsi1=[[False]*len(A)]*len(A)
       vsi1[starti][starti]=True
       quque=collections.deque([starti,startj,0])
       while True:
          for _ in range(len(quque)):
             r,c,cst=quque.popleft()
             vsi1[r][c]=True
             for nexti,nextj in neighbors(r,c):
                if vsi1[nexti][nextj]==False:
                   if A[nexti][nextj]==1:
                      return cst
                   if vis[nexti][nextj]==False:
                      quque.append((nexti,nextj,cst+1))
                   else:
                      quque.append((nexti,nextj,cst))


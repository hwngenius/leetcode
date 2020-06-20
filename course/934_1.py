from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        R,C=len(A),len(A[0])
        def get_neibor(r,c):
            for row,col in [(r,c+1),(r,c-1),(r-1,c),(r+1,c)]:
                if 0<=row<R and 0<=col<C:
                    yield row,col


        def get_see():
            for i in range(R):
                for j in range(C):
                    if A[i][j]==1:
                        stack=[(i,j)]
                        seen=set()
                        while stack:
                            node=stack.pop()
                            seen.add(node)
                            for nei in get_neibor(*node):
                                if A[nei[0]][nei[1]]==1 and nei not in seen:
                                    stack.append(nei)
                        return seen

        seen=get_see()
        queue=deque([(node,0) for node in seen])
        while queue:
            node,d=queue.popleft()
            for nei in get_neibor(*node):
                if nei not in seen:
                    if A[nei[0]][nei[1]]==1:
                        return d
                    queue.append((nei,d+1))
print(Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
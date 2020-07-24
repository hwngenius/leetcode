from typing import List
import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if n==0 or dst==src:return 0
        adjust=collections.defaultdict(list)
        graph=collections.defaultdict(dict)
        cost=[float('inf') for _ in range(n)]
        cost[src]=0
        queue=collections.deque([(src,0)])
        for u,v,w in flights:
            graph[u][v]=w
            adjust[u].append(v)
        for _ in range(K+1):
            for i in range(len(queue)):
                current,cs=queue.popleft()
                for nei in adjust[current]:
                    if cost[nei]>cs+graph[current][nei]:
                        cost[nei]=cs+graph[current][nei]
                        queue.append((nei,cost[nei]))
        return cost[dst] if cost[dst]!=float('inf') else -1

n=3
edges=[[0,1,100],[1,2,100],[0,2,500]]
src=0
dst=2
k=0
print(Solution().findCheapestPrice(n,edges,src,dst,k))
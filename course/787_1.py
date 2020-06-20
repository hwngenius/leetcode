from typing import List
import collections
import heapq

class Solution:
    def findCheapestPrice(self,n:int,flights:List[List[int]],src:int,dst:int,K:int)->int:
        graph=collections.defaultdict(dict)
        for u,v,w in flights:
            graph[u][v]=w

        best={}
        best[(0,src)]
        pq=[(0,0,src)]
        while pq:
            cost,k,place=heapq.heappop(pq)
            if cost>best.get((k,place),float("inf")):continue
            if dst==place:return cost
            elif k==K+1:
                continue
            else:
                for nei,wt in graph[place].items():
                    new_cost=wt+cost
                    if new_cost>best.get((k+1,nei),float('inf')):
                        best[(k+1,nei)]=new_cost
                        heapq.heappush(pq,(new_cost,k+1,nei))


        return -1
from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        dist = defaultdict(lambda: N * N)
        for i in range(N): dist[(1 << i, i)] = 0
        queue = deque([(1 << i, i) for i in range(N)])
        while queue:
            cover, place = queue.popleft()
            d = dist[(cover, place)]
            if cover == 2 ** N - 1: return d
            for nei in graph[place]:
                new_coer = cover | (1 << nei)
                if d + 1 < dist[(new_coer, nei)]:
                    dist[(new_coer, nei)] = d + 1
                    queue.append((new_coer, nei))


graph = [[1, 2, 3], [0], [0], [0]]
print(Solution().shortestPathLength(graph))

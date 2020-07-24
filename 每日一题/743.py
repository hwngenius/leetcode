from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        vis = [False for _ in range(N + 1)]
        dist = [float('inf') for _ in range(N + 1)]
        dist[K] = 0
        for _ in range(1, N + 1):
            u, MIN = -1, float('inf')
            for v in range(N + 1):
                if vis[v] is False and dist[v] < MIN:
                    MIN = dist[v]
                    u = v
            if u == -1:
                break
            vis[u] = True
            for a, b, c in times:
                if u == a:
                    if dist[b] > dist[u] + c:
                        dist[b] = dist[u] + c
        ans = max(dist[1:])
        return ans if ans != float('inf') else -1


times = [[1, 2, 1], [2, 1, 3]]
K = 2
N = 2
print(Solution().networkDelayTime(times, N, K))

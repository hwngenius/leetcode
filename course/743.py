class Solution:
    def networkDelayTime(self, times, N, K):
        vis = [False] * (N+1)
        dist = [float('inf')] * (N+1)
        from collections import defaultdict
        graph = defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w
        dist[K]=0
        for _ in range(N):
            u, MIN = -1, float('inf')
            for i in range(1,N+1):
                if dist[i] < MIN and vis[i] is not True:
                    MIN = dist[i]
                    u = i
            if u == -1:
                break
            vis[u] = True
            for nei, cost in graph[u].items():
                new_cost = cost + dist[u]
                if new_cost < dist[nei] and vis[nei] == False:
                    dist[nei]=new_cost


        ans = max(dist[1:N + 1])
        return ans if ans != float('inf') else -1


times = [[1,2,1],[2,1,3]]
N = 2
K = 2
print(Solution().networkDelayTime(times, N, K))

# finished by myself

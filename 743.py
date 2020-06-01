class Solution:
    def networkDelayTime(self, times, N, K):
        vis = [False] * (N + 1)
        dist = [100000000] * (N + 1)
        dist[K] = 0
        for i in range(N):
            u, MIN = -1, 100000000
            for j in range(1, N + 1):
                if dist[j] < MIN and vis[j] is False:
                    MIN = dist[j]
                    u = j
            if u == -1:
                break;
            vis[u] = True
            for time in times:
                if time[0] == u:
                    if dist[time[1]] > dist[u] + time[2]:
                        dist[time[1]] = dist[u] + time[2]

        ans = max(dist[1:N + 1])
        return ans if ans != 100000000 else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
print(Solution().networkDelayTime(times, N, K))

# finished by myself

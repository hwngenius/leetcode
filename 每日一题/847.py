import collections


class Solution(object):
    def shortestPathLength(self, graph):
        N = len(graph)
        queue = collections.deque((1 << x, x) for x in range(N))
        dist = collections.defaultdict(lambda: N * N)
        for i in range(N): dist[1 << i, i] = 0
        while queue:
            cover, head = queue.popleft()
            d = dist[cover, head]
            if cover == 2 ** N - 1: return d
            for child in graph[head]:
                new_cover = cover | 1 << child
                if dist[new_cover, child] > d + 1:
                    dist[new_cover, child] = d + 1
                    queue.append((new_cover, child))

from heapq import heappush


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ans = 0
        if not heightMap: return ans
        # current_max_height = float('-inf')
        vis = set()
        row, col = len(heightMap), len(heightMap[0])
        heap = []
        for r in range(row):
            heappush(heap, (heightMap[r][0], r, 0))
            heappush(heap, (heightMap[r][col - 1], r, col - 1))
            vis.add((r, 0))
            vis.add((r, col - 1))
        for c in range(1, col - 1):
            heappush(heap, (heightMap[0][c], 0, c))
            heappush(heap, (heightMap[row - 1][c], row - 1, c))
            vis.add((0, c))
            vis.add((row - 1, c))

        while heap:
            current_height, i, j = heappop(heap)
            # current_max_height = max(current_height, current_max_height)
            for r, c in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
                if r < 0 or r >= row or c < 0 or c >= col or (r, c) in vis:
                    continue
                vis.add((r, c))
                if heightMap[r][c] < current_height:
                    ans += current_height - heightMap[r][c]
                heappush(heap, (max(current_height,heightMap[r][c]), r, c))
        return ans
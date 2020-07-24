from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        data = [0 for _ in range(N + 1)]
        for a, b in trust:
            data[a] -= 1
            data[b] += 1
        ans = -1
        for i, x in enumerate(data[1:]):
            if x == N - 1:
                ans = i+1
        return ans


trust = [[1,2]]
N=2

print(Solution().findJudge(N,trust))

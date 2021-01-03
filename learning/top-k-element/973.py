from math import sqrt
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points=sorted(points,key=lambda x: sqrt(x[0]**2+x[1]**2))
        return points[:K]


points = [[3,3],[-2,2],[4,4]]
K = 2

print(Solution().kClosest(points,K))
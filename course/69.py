
class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        ans=int(math.sqrt(x))
        return ans


for i in range(17):
    print(i,Solution().mySqrt(i))

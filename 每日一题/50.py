class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        factor = x
        ans = 1
        while n:
            if n & 1:
                ans *= factor
            n >>= 1
            factor *= factor
        return ans


print(Solution().myPow(2, 10))

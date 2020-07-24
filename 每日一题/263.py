class Solution:
    def isUgly(self, num: int) -> bool:
        if num==0:
            return False
        numbers = [2, 3, 5]
        for n in numbers:
            while num % n == 0:
                num //= n
        return num == 1


print(Solution().isUgly(6))
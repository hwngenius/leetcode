class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        first,second=1,2
        ans=0
        for i in range(n-2):
            ans=first+second
            first,second=second,ans
        return ans


print(Solution().climbStairs(3))
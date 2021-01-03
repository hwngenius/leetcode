class Solution:
    def climbStairs(self, n: int) -> int:
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current


# 执行用时：
# 36 ms
# , 在所有 Python3 提交中击败了
# 77.21%
# 的用户
# 内存消耗：
# 14.8 MB
# , 在所有 Python3 提交中击败了
# 7.27%
# 的用户
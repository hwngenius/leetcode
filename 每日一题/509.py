class Solution:
    def fib(self, n: int) -> int:
        if n==0:return 0
        a,b=0,1
        for i in range(1,n):
            a,b=b,a+b
        return b

# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 63.74%
# 的用户
# 内存消耗：
# 14.6 MB
# , 在所有 Python3 提交中击败了
# 15.74%
# 的用户  
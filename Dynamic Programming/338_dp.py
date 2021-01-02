class Solution:
    def countBits(self, num: int) -> List[int]:
        dp=[0]*(num+1)
        for i in range(1,num+1):
            dp[i]=dp[i&(i-1)]+1
        return dp

# 执行用时：
# 80 ms
# , 在所有 Python3 提交中击败了
# 92.25%
# 的用户
# 内存消耗：
# 21.2 MB
# , 在所有 Python3 提交中击败了
# 14.95%
# 的用户
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for _ in range(len(text1)+1)]for _ in range(len(text2)+1)]
        for i in range(len(text2)):
             for j in range(len(text1)):
                if text2[i]==text1[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]

# 执行用时：
# 508 ms
# , 在所有 Python3 提交中击败了
# 18.51%
# 的用户
# 内存消耗：
# 23.1 MB
# , 在所有 Python3 提交中击败了
# 13.36%
# 的用户
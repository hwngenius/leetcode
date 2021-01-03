class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*len(s)
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i]=True
                continue
            for word in wordDict:
                n=len(word)
                if word == s[i-n+1:i+1] and dp[i-n]:
                    dp[i]=True

        return dp[len(s)-1]

# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 91.66%
# 的用户
# 内存消耗：
# 14.8 MB
# , 在所有 Python3 提交中击败了
# 13.35%
# 的用户
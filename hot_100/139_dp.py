from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*len(s)
        for i in range(len(s)):
            for word in wordDict:
                if s[i:i+len(word)]==word:
                    if i==0 or dp[i-1]:
                        dp[i+len(word)-1]=True
        return dp[-1]

# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 91.73%
# 的用户
# 内存消耗：
# 14.7 MB
# , 在所有 Python3 提交中击败了
# 18.75%
# 的用户
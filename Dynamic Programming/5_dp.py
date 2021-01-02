class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=""
        dp=[[False for _ in range(n)]for _ in range(n)]
        for l in range(n):
            for i in range(n):
                j=i+l
                if j>=n:
                    break
                if l==0:
                    dp[i][j]=True
                elif l==1:
                    dp[i][j]=s[i]==s[j]
                else:
                    dp[i][j]=(dp[i+1][j-1] and s[i]==s[j])
                if dp[i][j] and l+1>len(ans):
                    ans=s[i:j+1]
        return ans

print(Solution().longestPalindrome("babad"))
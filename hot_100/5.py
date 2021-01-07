class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def myfun(i,j):
            while i>=0 and j<n:
                if s[i]!=s[j]:
                    break
                i-=1
                j+=1
            return (i,j)
        ans=""
        for i in range(n):
            left,right=myfun(i,i)
            if right-left-1>len(ans):ans=s[left+1:right]
            left,right=myfun(i,i+1)
            if right-left-1>len(ans):ans=s[left+1:right]
        return ans


# 执行用时：
# 736 ms
# , 在所有 Python3 提交中击败了
# 84.99%
# 的用户
# 内存消耗：
# 14.9 MB
# , 在所有 Python3 提交中击败了
# 46.07%
# 的用户
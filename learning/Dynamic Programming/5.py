class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def myfun(i,j):
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            return i,j
        max_length=0
        for i in range(n):
            left,right=myfun(i,i)
            if right-left>max_length:
                max_length=right-left
                ans=s[left+1:right]
            left,right=myfun(i,i+1)
            if right-left>max_length:
                max_length=right-left
                ans=s[left+1:right]

        return ans
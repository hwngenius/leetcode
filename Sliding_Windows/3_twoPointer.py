class Solution:
    def lengthOfLongestSubstring(self,s):
        n=len(s)
        hash=set()
        ans,right=0,-1
        for left in range(n):
            if left>0:
                hash.remove(s[left-1])
            while right+1<n and s[right+1] not in hash:
                right+=1
                hash.add(s[right])
            ans=max(ans,right-left+1)
        return ans
print(Solution().lengthOfLongegsSubstring(""))
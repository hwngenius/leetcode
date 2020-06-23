class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        data = set()
        ans = left = right = 0
        while right < n:
            while right<n and s[right] not in data:
                data.add(s[right])
                right+=1
            ans=max(right-left,ans)
            if right==n:
                break
            left_t=s[left:right].index(s[right])+left+1
            for i in range(left,left_t):
                data.remove(s[i])
            left=left_t
        return ans


print(Solution().lengthOfLongestSubstring("pwwkew"))
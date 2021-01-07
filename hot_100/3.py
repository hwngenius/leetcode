class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i,j=-1,0
        ans=0
        hash_table=set()
        while j<len(s):
            if s[j] in hash_table:
                t=s[i+1:j+1].index(s[j])
                for k in range(t+1):
                    hash_table.remove(s[i+k+1])
                i=i+1+t
            hash_table.add(s[j])
            ans=max(ans,j-i)
            j+=1

        return ans

print(Solution().lengthOfLongestSubstring("pwwkew"))


# 执行用时：
# 100 ms
# , 在所有 Python3 提交中击败了
# 29.34%
# 的用户
# 内存消耗：
# 14.8 MB
# , 在所有 Python3 提交中击败了
# 18.13%
# 的用户
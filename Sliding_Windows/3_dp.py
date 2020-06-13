class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        length = [1] * n
        start = [0] * n
        if n==0:
            return 0
        for i in range(1, n):
            t = s[start[i - 1]:i].find(s[i])+start[i-1]
            if t == -1:
                start[i] = start[i - 1]
                length[i] = length[i - 1] + 1
            else:
                start[i] = t + 1
                length[i] = i-start[i] + 1
        return max(length)


print(Solution().lengthOfLongestSubstring("dvda"))

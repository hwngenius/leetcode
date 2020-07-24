class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        max_length = 0
        ans = ""

        def myfun(i, j):
            while i >= 0 and j < s_len and s[i] == s[j]:
                i -= 1
                j += 1
            return i, j

        for i in range(s_len):
            left, right = myfun(i, i)
            if right - left > max_length:
                max_length = right - left
                ans = s[left + 1:right]
            left, right = myfun(i, i + 1)
            if right - left > max_length:
                max_length = right - left
                ans = s[left + 1:right]
        return ans

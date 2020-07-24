class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)

        for i in range(0, h_len - n_len + 1):
            if haystack[i:i + n_len] == needle:
                return i
        return -1


print(Solution().strStr("hello", ""))

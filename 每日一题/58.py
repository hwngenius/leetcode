class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if all(c==' ' for c in s):
            return 0
        right = len(s) - 1
        while not s[right].isalpha(): right -= 1
        left = right
        while left >= 0 and s[left].isalpha(): left -= 1
        return right - left


print(Solution().lengthOfLastWord("worldfdhelo!!!!!!"))

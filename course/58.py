class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        L = s.split(" ")
        i = len(L) - 1
        while i >= 0:
            if len(L[i]) != 0:
                return len(L[i])
            i -= 1
        return 0

print(Solution().lengthOfLastWord("a "))

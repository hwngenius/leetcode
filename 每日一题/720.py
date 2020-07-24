from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ""
        words_set = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:i] in words for i in range(1, len(word) - 1)):
                    ans = word
        return ans

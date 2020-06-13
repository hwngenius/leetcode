import collections
from typing import List
import copy


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_count = collections.Counter(words)
        ans = []
        if len(s) == 0 or len(words)==0:
            return []
        left, right = 0, len(words[0]) * len(words)
        while right<=len(s):
            words_count_t = copy.deepcopy(words_count)
            for i in range(left, right, len(words[0])):
                if s[i:i + len(words[0])] in words_count_t:
                    words_count_t[s[i:i + len(words[0])]] -= 1
                    if words_count_t[s[i:i + len(words[0])]] == 0:
                        words_count_t.pop(s[i:i + len(words[0])])
                else:
                    break
            if len(words_count_t) == 0:
                ans.append(left)
            left += 1
            right += 1
        return ans


s="wordgoodgoodgoodbestword"
words=["word","good","best","good"]
print(Solution().findSubstring(s, words))

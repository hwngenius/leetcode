from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[int]) -> str:
        if len(strs) == 0:
            return ""
        min_length = 100000000000
        index = -1
        for i, v in enumerate(strs):
            if len(v) < min_length:
                min_length = len(v)
                index = i

        index_t = 0
        flag = True
        while index_t < min_length:
            c = strs[0][index_t]
            for j in range(len(strs)):
                if c != strs[j][index_t]:
                    flag = False
                    break
            if flag == False:
                break
            index_t += 1
        return strs[0][:index_t]

strs = ["dog","racecar","car"]
print(Solution().longestCommonPrefix(strs))

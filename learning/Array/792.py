from typing import List

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        ans=0
        heads=[[]for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it))-ord('a')].append(it)

        for letter in S:
            letter_index=ord(letter)-ord('a')
            old_bucket=heads[letter_index]
            heads[letter_index]=[]

            while old_bucket:
                it=old_bucket.pop()
                nxt=next(it,None)
                if nxt:
                    heads[ord(nxt)-ord('a')].append(it)
                else:
                    ans+=1
        return ans



print(Solution().numMatchingSubseq(S,words))

# 执行用时：
# 476 ms
# , 在所有 Python3 提交中击败了
# 55.69%
# 的用户
# 内存消耗：
# 16.1 MB
# , 在所有 Python3 提交中击败了
# 20.64%
# 的用户
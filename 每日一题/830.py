from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans=[]
        cur_char,cur_length=None,0
        for i,c in enumerate(s):
            if not cur_char:
                cur_char=c
                cur_length=1
            elif cur_char==c:
                cur_length+=1
            else:
                if cur_length>=3:
                    ans.append([i-cur_length,i-1])
                cur_length=1
                cur_char=c
        if cur_length>=3:
            ans.append([len(s)-cur_length,len(s)-1])
        return ans

# 执行用时：
# 32 ms
# , 在所有 Python3 提交中击败了
# 97.95%
# 的用户
# 内存消耗：
# 14.9 MB
# , 在所有 Python3 提交中击败了
# 6.66%
# 的用户
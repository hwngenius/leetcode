from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans=[]
        s=""

        def tracebacke(idx,s):
            if idx==len(S):
                ans.append(s)
                return
            
            while idx<len(S) and S[idx].isnumeric():
                idx+=1
            s+=S[len(s):idx]
            if len(s)==len(S):
                ans.append(s)
                return
            tracebacke(idx+1,s+S[idx].upper())
            tracebacke(idx+1,s+S[idx].lower())
        
        tracebacke(0,s)
        return ans

# 执行用时：
# 48 ms
# , 在所有 Python3 提交中击败了
# 82.35%
# 的用户
# 内存消耗：
# 15.9 MB
# , 在所有 Python3 提交中击败了
# 7.61%
# 的用户
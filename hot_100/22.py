from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        hash_table={-1:')',1:'('}
        ans=[]
        def trackback(combination,total,idx):
            if idx==2*n:
                if total==0:
                    ans.append(combination[:])
            else:
                for k in hash_table:
                    if total+k>=0
                        trackback(combination+hash_table[k],total+k,idx+1)
        trackback("",0,0)
        return ans


# 执行用时：
# 48 ms
# , 在所有 Python3 提交中击败了
# 27.50%
# 的用户
# 内存消耗：
# 15 MB
# , 在所有 Python3 提交中击败了
# 11.75%
# 的用户
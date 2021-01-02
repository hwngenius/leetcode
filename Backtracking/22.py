from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        Map={1:'(',-1:')'}
        combination=list()
        res=list()
        def trackback(total,idx):
            if idx==2*n:
                if total==0:
                    res.append(''.join(combination))
                return
            for k in Map:
                if total+k>=0:
                    combination.append(Map[k])
                    trackback(total+k,idx+1)
                    combination.pop()
        trackback(0,0)
        return res


# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 51.06%
# 的用户
# 内存消耗：
# 15.1 MB
# , 在所有 Python3 提交中击败了
# 5.40%
# 的用户
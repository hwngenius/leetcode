from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        tmp=[]
        def trackback(total,idx):
            if total==target:
                res.append(tmp.copy())
                return
            
            for i in range(idx,len(candidates)):
                if total+candidates[i]>target:
                    continue
                total+=candidates[i]
                tmp.append(candidates[i])
                trackback(total,i)
                tmp.pop()
                total-=candidates[i]
            
        trackback(0,0)
        return res


# 执行用时：
# 56 ms
# , 在所有 Python3 提交中击败了
# 79.66%
# 的用户
# 内存消耗：
# 15 MB
# , 在所有 Python3 提交中击败了
# 5.02%
# 的用户
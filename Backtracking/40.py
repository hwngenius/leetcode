from typing import List
import collections

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        count=collections.Counter(candidates)
        candidates=sorted(count.keys())
    
        tmp=[]
        ans=[]
        def trackback(idx,total,times):
            if total==target:
                ans.append(tmp.copy())
                return
            
            for i in range(idx,len(candidates)):
                if tmp and candidates[i]!=tmp[-1]:
                    times=0
                if total+candidates[i]>target:
                    return
                tmp.append(candidates[i])
                if times+1<count[candidates[i]]:
                    trackback(i,total+candidates[i],times+1)
                else:
                    trackback(i+1,total+candidates[i],0)
                tmp.pop()
        trackback(0,0,0)
        return ans

# 执行用时：
# 64 ms
# , 在所有 Python3 提交中击败了
# 58.61%
# 的用户
# 内存消耗：
# 15 MB
# , 在所有 Python3 提交中击败了
# 5.22%
# 的用户
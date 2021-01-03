from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        tmp=[]
        def tracebacke(idx,total,count):
            if total==n and count==k:
                ans.append(tmp[:])
            if count>k:
                return
            for i in range(idx,9):
                if total+i+1>n:
                    return
                tmp.append(i+1)
                tracebacke(i+1,total+i+1,count+1)
                tmp.pop()

        tracebacke(0,0,0)
        return ans


# 执行用时：
# 36 ms
# , 在所有 Python3 提交中击败了
# 86.68%
# 的用户
# 内存消耗：
# 14.7 MB
# , 在所有 Python3 提交中击败了
# 13.18%
# 的用户
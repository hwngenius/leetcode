from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        tmp=[]
        def tracebacke(count,idx):
            if count==k:
                ans.append(tmp[:])
                return
            for i in range(idx,n):
                tmp.append(i+1)
                tracebacke(count+1,i+1)
                tmp.pop()
        tracebacke(0,0)
        return ans


# 执行用时：
# 368 ms
# , 在所有 Python3 提交中击败了
# 68.44%
# 的用户
# 内存消耗：
# 16 MB
# , 在所有 Python3 提交中击败了
# 13.42%
# 的用户
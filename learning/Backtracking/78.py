from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        tmp=[]
        ans=[]
        # whether=(False,True)
        def tracebacke(i=0):
            if i==len(nums):
                ans.append(tmp[:])
                return
            

            tmp.append(nums[i])
            tracebacke(i+1)
            tmp.pop()
            tracebacke(i+1)
        tracebacke()
        return ans

# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 38.08%
# 的用户
# 内存消耗：
# 15 MB
# , 在所有 Python3 提交中击败了
# 5.10%
# 的用户
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def tracebacke(idx):
            if idx==len(nums):
                ans.append(nums[:])
            for i in range(idx,len(nums)):
                nums[i],nums[idx]=nums[idx],nums[i]
                tracebacke(idx+1)
                nums[i],nums[idx]=nums[idx],nums[i]
        tracebacke(0)
        return ans

# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 53.30%
# 的用户
# 内存消耗：
# 14.9 MB
# , 在所有 Python3 提交中击败了
# 6.06%
# 的用户
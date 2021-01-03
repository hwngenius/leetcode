from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_min=nums[0]
        current_max=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            t_current_max=current_max
            current_max=max(nums[i],nums[i]*current_max,nums[i]*current_min)
            current_min=min(nums[i],nums[i]*current_min,nums[i]*t_current_max)
            ans=max(current_max,ans)
        return ans

# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 88.47%
# 的用户
# 内存消耗：
# 14.9 MB
# , 在所有 Python3 提交中击败了
# 27.38%
# 的用户
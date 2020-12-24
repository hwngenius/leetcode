from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def travel(i,forward:int,vist):
            if nums[i]*forward<0:
                return False
            next_index=(nums[i]+i)%len(nums)
            if vist[next_index] is True:
                if next_index!=i:
                    return True
                else:
                    return False
            else:
                vist[i]=True
                return travel(next_index,forward,vist)
        for i in range(len(nums)):
            vist=[False]*len(nums)
            if travel(i,nums[i],vist):return True
        return False

# 执行用时：
# 680 ms
# , 在所有 Python3 提交中击败了
# 22.68%
# 的用户
# 内存消耗：
# 16.7 MB
# , 在所有 Python3 提交中击败了
# 5.19%
# 的用户
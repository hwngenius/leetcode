from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        ans=0
        def traceback(nums,i,total,S):
            nonlocal ans
            if len(nums)==i:
                if total==S:
                    ans+=1
                return

            else:
                traceback(nums,i+1,total+nums[i],S)
                traceback(nums,i+1,total-nums[i],S)
            
        traceback(nums,0,0,S)
        return ans

print(Solution().findTargetSumWays([1,1,1,1,1],3))
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tmp=[]
        ans=[]
        vis=[False]*len(nums)
        def backtrack(idx):
            if idx==len(nums):
                ans.append(tmp[:])
                return
            for i in range(len(nums)):
                if vis[i] or(i>0 and not vis[i-1] and nums[i-1]==nums[i]):
                    continue
                tmp.append(nums[i])
                vis[i]=True
                backtrack(idx+1)
                vis[i]=False
                tmp.pop()
        backtrack(0)
        return ans

print(Solution().permuteUnique([1,1,2]))
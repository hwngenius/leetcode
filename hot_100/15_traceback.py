from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if n<3:return []
        ans=[]
        vis=[False]*n
        nums.sort()
        def traceback(component,idx,count,total):
            if count==3 and total==0:
                ans.append(component[:])
            if count<3 and total<1 and idx<n:
                if not (idx>0 and nums[idx-1]==nums[idx] and vis[idx-1] is False):
                    component.append(nums[idx])
                    vis[idx]=True
                    traceback(component,idx+1,count+1,total+nums[idx])
                    component.pop()
                    vis[idx]=False
                traceback(component,idx+1,count,total)
        traceback([],0,0,0)
        return ans


# 315/318 out of time
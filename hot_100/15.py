from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:return []
        nums.sort()
        ans=set()
        for i in range(len(nums)):
            left,right=i+1,len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total<0:
                    left+=1
                elif total>0:
                    right-=1
                else:
                    ans.add((nums[i],nums[left],nums[right]))
                    right-=1
        return [ele for ele in ans]


# 执行用时：
# 2836 ms
# , 在所有 Python3 提交中击败了
# 5.02%
# 的用户
# 内存消耗：
# 16.7 MB
# , 在所有 Python3 提交中击败了
# 26.54%
# 的用户



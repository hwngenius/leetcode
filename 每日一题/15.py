from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        if all(num==0 for num in nums):
            return [[0,0,0]]

        found=[]
        nums=sorted(nums)
        rightmost=len(nums)-1
        for index,eachNum in enumerate(nums):
            left=index+1
            right=rightmost
            while left<right:
                check_sum=(eachNum+nums[left]+nums[right])
                if check_sum==0:
                    new_found=[eachNum,nums[left],nums[right]]
                    if new_found not in found:
                        found.append(new_found)
                    right-=1
                elif check_sum<0:
                    left+=1
                else:
                    right-=1
        return found


print(Solution().threeSum([-1,0,1,2,-1,-4]))
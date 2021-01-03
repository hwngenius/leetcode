from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer,L,R=[0]*len(nums),[0]*len(nums),[0]*len(nums)
        L[0]=nums[0]
        for i in range(1,len(nums)):
            L[i]=L[i-1]*nums[i]

        R[len(nums)-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            R[i]=R[i+1]*nums[i]
        
        answer[0]=R[1]
        answer[-1]=L[-2]
        for i in range(1,len(nums)-1):
            answer[i]=L[i-1]*R[i+1]
        return answer

# 执行用时：
# 88 ms
# , 在所有 Python3 提交中击败了
# 34.75%
# 的用户
# 内存消耗：
# 20.8 MB
# , 在所有 Python3 提交中击败了
# 5.05%
# 的用户
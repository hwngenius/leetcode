from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        res=[0]*length
        res[0]=1
        for i in range(1,length):
            res[i]=res[i-1]*nums[i-1]
        right_product=1
        for i in range(length-1,-1,-1):
            res[i]*=right_product
            right_product*=nums[i]
        
        return res


# 执行用时：
# 72 ms
# , 在所有 Python3 提交中击败了
# 72.27%
# 的用户
# 内存消耗：
# 19.4 MB
# , 在所有 Python3 提交中击败了
# 18.09%
# 的用户
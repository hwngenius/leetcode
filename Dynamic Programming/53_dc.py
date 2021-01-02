class Solution:
    def maxSubArray(self,nums:List[int])->int:
        if len(nums)==1:
            return nums[0]
        else:
            max_left=self.maxSubArray(nums[0:len(nums)//2])
            max_right=self.maxSubArray(nums[len(nums)//2:])
            max_middle_left=nums[len(nums)//2-1]
            tmp=0
            for i in range(len(nums)//2-1,-1,-1):
                tmp+=nums[i]
                max_middle_left=max(max_middle_left,tmp)
            max_middle_right=nums[len(nums)//2]
            tmp=0
            for i in range(len(nums)//2,len(nums)):
                tmp+=nums[i]
                max_middle_right=max(max_middle_right,tmp)
            return max(max_left,max_right,max_middle_left+max_middle_right)

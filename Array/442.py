class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:return []

        rst=[]
        for num in nums:
            index=abs(num)-1
            val=nums[index]
            if val<0:
                rst.append(abs(nums))
            nums[index]=-nums[index]
        return rst
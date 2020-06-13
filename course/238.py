class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_num = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_num += 1

        output = [0] * len(nums)
        if zero_num == 0:
            for i in range(len(nums)):
                if nums[i] != 0:
                    output[i] = product // nums[i]
        elif zero_num == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output[i] = product
                else:
                    output[i] = 0

        return output

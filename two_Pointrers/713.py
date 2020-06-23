from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        ans = 0
        current_product = nums[0]
        left = right = 0
        while left <= right < len(nums):
            if current_product < k:
                ans += (right - left + 1)
                right += 1
                if right<len(nums):
                    current_product *= nums[right]
                else:
                    break
            else:
                if left!=right:
                    current_product /= nums[left]
                    left += 1
                else:
                    right += 1
                    if right < len(nums):
                        current_product *= nums[right]
                    else:
                        break
        return ans


nums = [10, 5, 100,10,5]
k = 100
print(Solution().numSubarrayProductLessThanK(nums, k))

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(ans - target):
                    ans = total
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    return ans
        return ans


nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(nums, target))

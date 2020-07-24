from typing import List


class Solution:
    def threeSumCloset(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float("inf")
        right_most = len(nums) - 1
        for index, x in enumerate(nums):
            left, right = index + 1, right_most
            while left < right:
                total = x + nums[left] + nums[right]
                t = total - target
                if abs(t) < abs(ans - target):
                    ans = total
                if t < 0:
                    left += 1
                else:
                    right -= 1
        return ans


print(Solution().threeSumCloset([-1, 2, 1, -4], 1))

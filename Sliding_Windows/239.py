from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k + 1
        ans = [0] * n
        max_index = 0
        max_num = -100000
        for i in range(k):
            if nums[i] > max_num:
                max_num = nums[i]
                max_index = i
        ans[0]=max_num
        for i in range(1, len(nums) - k+1):
            if i - 1 != max_index:
                if nums[i + k - 1] > max_num:
                    max_num, max_index = nums[i + k - 1], i + k - 1
            else:
                if max_num < nums[i + k - 1]:
                    max_num, max_index = nums[i + k - 1], i + k - 1
                else:
                    max_num = max(nums[i:i + k])
                    max_index = nums[i:i + k].index(max_num) + i
            ans[i] = max_num

        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))

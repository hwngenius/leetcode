from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in nums_set:
                tmp = 1
                while num + 1 in nums_set:
                    num += 1
                    tmp += 1
                ans = max(ans, tmp)

        return ans


nums = [100, 4, 200, 1, 3, 2]
print(Solution().longestConsecutive(nums))

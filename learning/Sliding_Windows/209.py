from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = len(nums)
        ans = l + 1
        left, right = 0, -1
        count = 0
        while left < l:
            while count < s and right + 1 < l:
                right += 1
                count += nums[right]
            if count >= s:
                ans = min(right - left + 1, ans)
            left += 1
            count -= nums[left - 1]
        if ans == l + 1:
            return 0
        else:
            return ans

# 执行用时 :
# 60 ms
# , 在所有 Python3 提交中击败了
# 49.45%
# 的用户
# 内存消耗 :
# 15.4 MB
# , 在所有 Python3 提交中击败了
# 61.11%
# 的用户

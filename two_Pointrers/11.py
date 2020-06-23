from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left, right = 0, len(heights) - 1
        while left < right:
            if heights[left] < heights[right]:
                ans = max(ans, (right - left) * heights[left])
                left += 1
            else:
                ans = max(ans, (right - left) * heights[right])
                right -= 1

        return ans


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(heights))

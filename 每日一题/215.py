from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        num = nums[n - 1]
        index = n - 2
        k -= 1
        while k > 0:
            while nums[index] == num:
                index -= 1
            num = nums[index]
            k -= 1
        return num

[3,2,3,1,2,4,5,5,6]
4
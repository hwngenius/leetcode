from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap=[nums[i] for i in range(k)]
        heapq.heapify(heap)
        for i in range(k,len(nums)):
            heapq.heappushpop(heap,nums[i])

        return heapq.heappop(heap)

nums=[3,2,1,5,6,4]
k=2
print(Solution().findKthLargest(nums,k))
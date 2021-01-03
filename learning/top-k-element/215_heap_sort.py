import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        

        def build_max_heap(a,heap_size):
            for i in range(heap_size//2,-1,-1):
                max_heapify(a,i,heap_size)
    
        def max_heapify(a,i,heap_size):
            l,r,largets=i*2+1,i*2+2,i
            if l<heap_size and a[l]>a[largets]:
                largets=l
            if r<heap_size and a[r] > a[largets]:
                largets=r
            if largets!=i:
                a[i],a[largets]=a[largets],a[i]
                max_heapify(a,largets,heap_size)

        heap_size=len(nums)
        build_max_heap(nums,heap_size)
        for i in range(len(nums)-1,len(nums)-k,-1):
            nums[i],nums[0]=nums[0],nums[i]
            heap_size-=1
            max_heapify(nums,0,heap_size)
        return nums[0]
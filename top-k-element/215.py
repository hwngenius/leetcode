import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        def quickSelect(a,l,r,idx):
            q=randomPatition(a,l,r)
            if q==idx:
                return a[q]
            elif q<idx:
                return quickSelect(a,q+1,r,idx)
            else:
                return quickSelect(a,l,q-1,idx)
        
        def randomPatition(a,l,r):
            i=random.randint(l,r)
            a[i],a[r]=a[r],a[i]
            return partition(a,l,r)
        
        def partition(a,l,r):
            x=a[r]
            i=l-1
            for j in range(l,r):
                if a[j]<=x:
                    i+=1
                    a[i],a[j]=a[j],a[i]
            a[i+1],a[r]=a[r],a[i+1]
            return i+1
        return quickSelect(nums,0,len(nums)-1,len(nums)-k)

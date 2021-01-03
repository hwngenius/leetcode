from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r=0,len(arr)-1
        while l<r:
            mid=(l+r)//2
            if arr[mid]<arr[mid+1]:
                l=mid+1
            else:
                r=mid
        return l


# 执行用时：
# 32 ms
# , 在所有 Python3 提交中击败了
# 97.66%
# 的用户
# 内存消耗：
# 15.8 MB
# , 在所有 Python3 提交中击败了
# 5.77%
# 的用户
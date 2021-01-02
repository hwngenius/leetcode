from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i=0
        while i<len(arr) and arr[i]<x:
            i+=1
        count=0
        ans=[]
        l,r=i-1,i
        while l>=0 and r<len(arr) and count<k:
            t1=abs(arr[l]-x)
            t2=abs(arr[r]-x)
            if t1<=t2:
                ans.append(arr[l])
                l-=1
            else:
                ans.append(arr[r])
                r+=1
            count+=1
        while count<k and l>0:
            ans.append(arr[l])
            l-=1
            count+=1
        while count<k and r<len(arr):
            ans.append(arr[r])
            r+=1
            count+=1
        ans.sort()
        return ans

arr = [1,1,1,10,10,10]
k = 1
x = 9
print(Solution().findClosestElements(arr,k,x))
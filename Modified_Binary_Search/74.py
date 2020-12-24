from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        if row==0:return False
        col=len(matrix[0])
        l,r=0,row*col-1
        while l<=r:
            mid=(l+r)//2
            if matrix[mid//col][mid%col]==target:return True
            if matrix[mid//col][mid%col]<target:l=mid+1
            else: r=mid-1
        return False 


# 执行结果：
# 通过
# 显示详情
# 执行用时：
# 36 ms
# , 在所有 Python3 提交中击败了
# 87.44%
# 的用户
# 内存消耗：
# 15.1 MB
# , 在所有 Python3 提交中击败了
# 5.38%
# 的用户
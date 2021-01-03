from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        if row==0:return
        re_write=set()
        col=len(matrix[0])
        def set_zero(i,j):
            for r in range(row):
                if matrix[r][j]!=0:
                    matrix[r][j]=0
                    re_write.add((r,j))
            for c in range(col):
                if matrix[i][c]!=0:
                    matrix[i][c]=0
                    re_write.add((i,c))
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0 and (i,j) not in re_write:
                    set_zero(i,j)
                
# 执行结果：
# 通过
# 显示详情
# 执行用时：
# 56 ms
# , 在所有 Python3 提交中击败了
# 39.67%
# 的用户
# 内存消耗：
# 16.6 MB
# , 在所有 Python3 提交中击败了
# 5.08%
# 的用户
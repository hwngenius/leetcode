class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:return False
        row,col=len(matrix),len(matrix[0])
        r=c=0
        while r<row and c <col:
            if target==matrix[r][c]:
                return True
            if target<matrix[r][c]:
                return False
            if target>matrix[r][col-1] and target>matrix[row-1][c]:
                r+=1
                c+=1
            elif target>matrix[r][col-1]:
                r+=1
            elif target>matrix[row-1][c]:
                c+=1
            else:
                for j in range(c,col):
                    if matrix[r][j]==target:
                        return True
                r+=1
        return False

# 执行用时：
# 208 ms
# , 在所有 Python3 提交中击败了
# 12.84%
# 的用户
# 内存消耗：
# 20.9 MB
# , 在所有 Python3 提交中击败了
# 7.25%
# 的用户
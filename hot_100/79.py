from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        row,col=len(board),len(board[0])
        def neighbord(i,j):
            for r,c in [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]:
                if 0<=r<row and 0<=c<col:
                    yield (r,c)
        vis=set()
        def myfun(r,c,idx):
            if board[r][c]==word[idx] and (r,c) not in vis:
                vis.add((r,c))
                if idx==len(word)-1:return True
                for nr,nc in neighbord(r,c):
                    if myfun(nr,nc,idx+1):
                        return True
                vis.remove((r,c))
            else:
                return False
        

        for i in range(row):
            for j in range(col):
                if myfun(i,j,0):
                    return True
        return False


# 执行用时：
# 356 ms
# , 在所有 Python3 提交中击败了
# 12.50%
# 的用户
# 内存消耗：
# 17.9 MB
# , 在所有 Python3 提交中击败了
# 8.80%
# 的用户
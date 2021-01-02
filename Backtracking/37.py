class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=len(board)
        col=len(board[0])
        vis=[[False for _ in range(col)]for _ in range(row)]
        def tracebacke(i,j):
            cocurrent=set()
            for r in range(row):
                cocurrent.add(board[r][j])
            for c in range(col):
                cocurrent.add(board[i][c])
            for full in 
# Que. :- 289. Game of Life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),          (0,1),
            (1,-1), (1,0), (1,1)
        ]

        for i in range(rows):
            for j in range(cols):

                live = 0

                for dx, dy in directions:
                    r = i + dx
                    c = j + dy

                    if 0 <= r < rows and 0 <= c < cols:
                        if abs(board[r][c]) == 1:
                            live += 1

                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = -1

                else:
                    if live == 3:
                        board[i][j] = 2

        for i in range(rows):
            for j in range(cols):

                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

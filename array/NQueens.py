class Solution(object):
    def is_valid_position(self, row, column, chess_board, n):
        for up in range(row - 1, -1, -1):
            if chess_board[up][column] == 1:
                return False

        diagonal_column = column - 1
        for left_diagonal in range(row - 1, -1, -1):
            if diagonal_column >= 0 and chess_board[left_diagonal][diagonal_column] == 1:
                return False
            diagonal_column -= 1

        diagonal_column = column + 1
        for right_diagonal in range(row - 1, -1, -1):
            if diagonal_column < n and chess_board[right_diagonal][diagonal_column] == 1:
                return False
            diagonal_column += 1

        return True

    def validate_chess_board(self, row, n, chess_board):
        solutions = 0
        if row == n:
            solutions += 1
        else:
            for column in range(n):
                if self.is_valid_position(row, column, chess_board, n):
                    chess_board[row][column] = 1
                    if row + 1 == n:
                        solutions += 1
                    else:
                        solutions += self.validate_chess_board(row + 1, n, chess_board)
                chess_board[row][column] = 0
        return solutions

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        solutions = 0
        chess_board = [[0 for column in range(n)] for row in range(n)]

        row = 0
        for column in range(n):
            chess_board[row][column] = 1
            solutions += self.validate_chess_board(row + 1, n, chess_board)
            chess_board[row][column] = 0
        return solutions


print(Solution().totalNQueens(1))

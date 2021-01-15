class Solution(object):
    def square(self, matrix, row, column):
        squares = 0

        if row == len(matrix) - 1 or column == len(matrix[0]) - 1:
            return squares

        if matrix[row][column] == '1':
            squares += 1

            if matrix[row][column] == '1' and matrix[row][column + 1] == '1' and matrix[row + 1][column] == '1' and \
                    matrix[row + 1][column + 1] == '1':
                right_matrix = self.square(matrix, row, column + 1)
                diagonal_matrix = self.square(matrix, row + 1, column + 1)
                bottom_matrix = self.square(matrix, row + 1, column)

                if right_matrix == diagonal_matrix and diagonal_matrix == bottom_matrix:
                    squares += right_matrix
                else:
                    squares += 3

        return squares

    def maximal_square(self, matrix):
        max_squares = 0
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                print(matrix[row][column], end=' ')
                squares = self.square(matrix, row, column)
                max_squares = max_squares if squares < max_squares else squares
            print()

        return max_squares


# print(Solution().maximal_square(
#     [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
print(Solution().maximal_square(
    [["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"],
     ["0", "0", "1", "1", "1"]]))

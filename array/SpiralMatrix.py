class SpiralMatrix:
    def print(self, matrix, m, n):
        directions = ['e', 's', 'w', 'n']
        start_row = 0
        end_row = m - 1

        start_column = 0
        end_column = n - 1

        while start_row <= end_row and start_column <= end_column:
            direction = directions.pop(0)

            if direction == 'e':
                for index in range(start_column, end_column + 1):
                    print(matrix[start_row][index], end=" ")
                start_row += 1
            elif direction == 's':
                for index in range(start_row, end_row + 1):
                    print(matrix[index][end_column], end=" ")
                end_column -= 1
            elif direction == 'w':
                for index in range(end_column, start_column - 1, -1):
                    print(matrix[end_row][index], end=" ")
                end_row -= 1
            elif direction == 'n':
                for index in range(end_row, start_row - 1, -1):
                    print(matrix[index][start_column], end=" ")
                start_column += 1

            directions.append(direction)


input_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
SpiralMatrix().print(input_matrix, len(input_matrix), len(input_matrix[0]))

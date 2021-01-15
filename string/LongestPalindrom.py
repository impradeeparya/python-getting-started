def init_2d_matrix(matrix, input_str):
    input_chars = list(input_str)

    for row in range(len(input_chars)):
        matrix[row][row] = 1
    start_index = 0
    max_length = 1
    for row in range(len(input_chars) - 1):
        if input_chars[row] == input_chars[row + 1]:
            matrix[row][row + 1] = 1
            if max_length == 1:
                start_index = row
                max_length = 2

    for k in range(3, len(input_chars) + 1):
        for i in range(len(input_chars) - k + 1):
            j = i + k - 1

            if matrix[i + 1][j - 1] == 1 and input_chars[i] == input_chars[j]:
                matrix[i][j] = 1

                if k > max_length:
                    start_index = i
                    max_length = k
    print(input_str[start_index:start_index + max_length])


def print_matrix(matrix, m, n):
    for row in range(m):
        for column in range(n):
            print(matrix[row][column], end=" ")
        print()


def print_longest_palindrome(input_str):
    str_length = len(input_str)
    matrix = [[0] * str_length for row in range(str_length)]
    init_2d_matrix(matrix, input_str)
    # print_matrix(matrix, str_length, str_length)


print_longest_palindrome("ac")

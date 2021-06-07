class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        max_row_sum = 0
        for index in range(len(wall[0])):
            max_row_sum += wall[0][index]

        max_column = 0
        for index in range(len(wall)):
            max_column = max_column if max_column > len(wall[index]) else len(wall[index])

        if max_column == 1:
            return 0

        new_matrix = [[-1 for column in range(max_row_sum + max_column - 1)] for row in range(len(wall))]
        for row in range(len(wall)):
            column_index = 0
            for column in range(len(wall[row])):
                if column > 0:
                    new_matrix[row][column_index] = 0
                    column_index += 1
                for number in range(1, wall[row][column] + 1):
                    new_matrix[row][column_index] = 1
                    column_index += 1
        print(new_matrix)

        one_count = 0
        for column in range(max_row_sum + max_column - 1):
            current_one_count = 0
            is_allowed = True
            for row in range(len(wall)):
                if new_matrix[row][column] == -1:
                    is_allowed = False
                    break
                if new_matrix[row][column] == 1:
                    current_one_count += 1
            if is_allowed and (current_one_count < one_count or one_count == 0):
                one_count = current_one_count

        return one_count


# print(Solution().leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]))
# print(Solution().leastBricks([[100000000], [100000000], [100000000]]))
print(Solution().leastBricks(
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))

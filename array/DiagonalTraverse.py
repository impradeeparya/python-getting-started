class Solution:
    def findDiagonalOrder_v1(self, nums):
        output = []
        rows = len(nums)

        max_columns = 0
        for row in range(rows):
            if len(nums[row]) > max_columns:
                max_columns = len(nums[row])

        for row in range(rows):
            x = row
            y = 0
            while x >= 0:
                if len(nums[x]) > y:
                    output.append(nums[x][y])
                x = x - 1
                y = y + 1

        for column in range(1, max_columns):
            x = rows - 1
            y = column
            while y < max_columns and x >= 0:
                if len(nums[x]) > y:
                    output.append(nums[x][y])
                x = x - 1
                y = y + 1

        return output

    def findDiagonalOrder(self, nums):
        output = []

        element_index = None
        element_diagonal_map = {}
        for row in range(len(nums)):
            element_index = row
            column = 0

            while len(nums[row]) > column:
                if element_diagonal_map.get(element_index, None) is None:
                    element_diagonal_map[element_index] = [nums[row][column]]
                else:
                    elements = element_diagonal_map.get(element_index, None)
                    elements.insert(0, nums[row][column])
                    element_diagonal_map[element_index] = elements
                element_index = element_index + 1
                column = column + 1

        for index in range(len(element_diagonal_map)):
            output.extend(element_diagonal_map[index])

        return output


print(Solution().findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))

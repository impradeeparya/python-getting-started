# You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.
#
# In the ith operation (1-indexed), you will:
#
# Choose two elements, x and y.
# Receive a score of i * gcd(x, y).
# Remove x and y from nums.
# Return the maximum score you can receive after performing n operations.
#
# The function gcd(x, y) is the greatest common divisor of x and y.

import math
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        max_score = 0

        gcd_values = [[-1 for column in range(len(nums))] for row in range(len(nums))]

        for row in range(len(nums)):
            for column in range(row + 1, len(nums)):
                if gcd_values[column][row] == -1:
                    gcd_values[row][column] = math.gcd(nums[row], nums[column])
                    gcd_values[column][row] = gcd_values[row][column]
        print(gcd_values)
        output = []
        visited = {}
        while len(visited) < len(nums):
            max_gcd = None
            max_column = None
            max_row = None
            for column in range(len(nums)):
                if visited.get(column, None) is None:
                    for row in range(len(nums)):
                        if visited.get(row, None) is None:
                            if gcd_values[row][column] != -1:
                                if max_gcd is None or (max_gcd < gcd_values[row][column]):
                                    max_gcd = gcd_values[row][column]
                                    max_column = column
                                    max_row = row

            if max_row is not None and max_column is not None:
                visited[max_column] = True
                visited[max_row] = True
                output.insert(0, max_gcd)

        print(output)
        for index in range(1, int(len(nums) / 2) + 1):
            max_score = max_score + (index * output[index - 1])
        return max_score

    def max_gcd_score(self, nums, operation, visited):

        nums_length = len(nums)

        if visited == ((1 << nums_length) - 1):
            return 0

        max_gcd = 0
        for i in range(nums_length):
            if visited & (1 << i) == 0:
                for j in range(i + 1, nums_length):
                    if visited & (1 << j) == 0:
                        max_gcd = max(max_gcd,
                                      operation * math.gcd(nums[i], nums[j]) + self.max_gcd_score(nums, operation + 1,
                                                                                                  visited | (1 << i) | (
                                                                                                          1 << j)))

        return max_gcd

    def max_score(self, nums: List[int]) -> int:
        return self.max_gcd_score(nums, 1, 0)

# print(Solution().maxScore([1, 2]))
# print(Solution().maxScore([697035, 181412, 384958, 575458]))
# print(Solution().maxScore([415, 230, 471, 705, 902, 87]))
# print(sorted([697035, 181412, 384958, 575458]))
# print(Solution().max_score([415, 230, 471, 705, 902, 87]))
# print(Solution().max_score([697035, 181412, 384958, 575458]))
# print(Solution().max_score(
#     [109497, 983516, 698308, 409009, 310455, 528595, 524079, 18036, 341150, 641864, 913962, 421869, 943382, 295019]))

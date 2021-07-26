# You are given an integer array nums and an integer target.
#
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums
# and then concatenate all the integers.
#
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the
# expression "+2-1". Return the number of different expressions that you can build, which evaluates to target.
from typing import List


class Solution:

    # Recursion
    # def target_count(self, nums, target, start_index, num_length):
    #     if target == 0 and start_index == num_length:
    #         return 1
    #     if start_index == num_length:
    #         return 0
    #
    #     output = self.target_count(nums, target + nums[start_index], start_index + 1, num_length)
    #
    #     output = output + self.target_count(nums, target - nums[start_index], start_index + 1, num_length)
    #     return output
    #
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     return self.target_count(nums, target, 0, len(nums))

    # Recursion
    # def target_count(self, nums, index, target):
    #
    #     if target == 0:
    #         return 1
    #
    #     if index == 0:
    #         return 0
    #
    #     if nums[index - 1] > target:
    #         return self.target_count(nums, index - 1, target)
    #
    #     return self.target_count(nums, index - 1, target - nums[index - 1]) + self.target_count(nums, index - 1,
    #                                                                                             target)
    #
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     return self.target_count(nums, n, round((sum(nums) + target) / 2))

    # Recursion + memoization
    # def target_count(self, nums, index, target, memory):
    #
    #     if target == 0:
    #         return 1
    #
    #     if index == 0:
    #         return 0
    #
    #     if memory[index][target] != -1:
    #         return memory[index][target]
    #
    #     if nums[index - 1] <= target:
    #         memory[index][target] = self.target_count(nums, index - 1, target - nums[index - 1],
    #                                                   memory) + self.target_count(
    #             nums, index - 1,
    #             target, memory)
    #         return memory[index][target]
    #
    #     if nums[index - 1] > target:
    #         memory[index][target] = self.target_count(nums, index - 1, target, memory)
    #         return memory[index][target]
    #
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     memory = [[-1 for row in range(0, 1000)] for column in range(0, 1000)]
    #     return self.target_count(nums, n, round((sum(nums) + target) / 2), memory)

    # DP
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = (sum(nums))
        if ((target + nums_sum) % 2) == 1:
            return 0
        n = len(nums)
        new_target = int((nums_sum + target) / 2)

        dp = [[0 for column in range(new_target + 1)] for row in range(n + 1)]
        for row in range(n + 1):
            for column in range(new_target + 1):
                if column == 0:
                    dp[row][column] = 1

        for row in range(1, n + 1):
            for column in range(0, new_target + 1):
                if nums[row - 1] <= column:
                    dp[row][column] = dp[row - 1][column - nums[row - 1]] + dp[row - 1][column]
                else:
                    dp[row][column] = dp[row - 1][column]

        return dp[n][new_target]


print("output 5 ", Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
print("output 1 ", Solution().findTargetSumWays(nums=[1], target=1))
print("output 4983",
      Solution().findTargetSumWays(nums=[44, 20, 38, 6, 2, 47, 18, 50, 41, 38, 32, 24, 38, 38, 30, 5, 26, 15, 37, 35],
                                   target=44))
print("output 6666 ",
      Solution().findTargetSumWays(nums=[0, 38, 42, 31, 13, 10, 11, 12, 44, 16, 38, 17, 22, 28, 9, 27, 20, 35, 34, 39],
                                   target=2))
print("output 6266 ",
      Solution().findTargetSumWays(nums=[35, 25, 24, 23, 2, 47, 39, 22, 3, 7, 11, 26, 6, 30, 5, 34, 10, 43, 41, 28],
                                   target=49))
print("output 0 ", Solution().findTargetSumWays(nums=[1], target=2))
print("output 0 ", Solution().findTargetSumWays(nums=[0, 0, 0, 0, 0, 0, 0, 0, 1], target=1))

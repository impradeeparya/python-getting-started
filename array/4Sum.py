class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        output = []
        output_index = 0
        index = 0
        n = len(nums) - 1
        nums.sort()
        sum_of = 2
        while index < n:
            one = nums[index]
            if n - index + 1 >= sum_of:
                pair_sum = self.threeSum(nums, target - one, index + 1)
                if len(pair_sum) > 0:
                    for pair in pair_sum:
                        temp_sum_list = one, pair[0], pair[1], pair[2]
                        output.insert(output_index, temp_sum_list)
                        output_index = output_index + 1
            else:
                break
            index = index + 1
        return [list(x) for x in set(tuple(x) for x in output)]

    def threeSum(self, nums: list[int], k: int, index: int):
        output = []
        output_index = 0
        n = len(nums) - 1
        sum_of = 2
        while index < n:
            one = nums[index]
            if n - index + 1 >= sum_of:
                pair_sum = self.twoSum(nums, k - one, index + 1)
                if len(pair_sum) > 0:
                    for pair in pair_sum:
                        temp_sum_list = one, pair[0], pair[1]
                        output.insert(output_index, temp_sum_list)
                        output_index = output_index + 1
            else:
                break
            index = index + 1
        return output

    def twoSum(self, nums: list[int], k: int, index: int):
        output = []
        output_index = 0
        n = len(nums) - 1
        while index < n:
            if nums[index] + nums[n] == k:
                temp_sum_list = nums[index], nums[n]
                output.insert(output_index, temp_sum_list)
                output_index = output_index + 1
                n = n - 1
                index = index + 1
            elif nums[index] + nums[n] > k:
                n = n - 1
            else:
                index = index + 1

        return output


print(Solution().fourSum([0, 1, 2, 3, 4, 5, 6, 7], 7))
print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
print(Solution().fourSum([2, 2, 2, 2, 2], 8))

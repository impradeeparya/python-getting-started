class Solution:
    # def longest_sub_array(self, array):
    #     max_sum = 0
    #     current_sum = 0
    #     is_first_zero = True
    #     next_start_index = 0
    #     start_index = 0
    #     while start_index < len(array):
    #         if array[start_index] == 1:
    #             current_sum += 1
    #         else:
    #             if is_first_zero:
    #                 next_start_index = start_index + 1
    #                 is_first_zero = False
    #             else:
    #                 current_sum += 1
    #                 if current_sum > max_sum:
    #                     max_sum = current_sum
    #                 current_sum = 0
    #                 start_index = next_start_index - 1
    #                 is_first_zero = True
    #         start_index += 1
    #     if not is_first_zero and current_sum + 1 > max_sum:
    #         max_sum = current_sum + 1
    #
    #     return max_sum

    def longest_sub_array(self, array):
        max_sum = 0
        start_index = 0
        zero_index = -1
        index = -1
        for index in range(len(array)):
            if array[index] == 0:
                if zero_index == -1:
                    zero_index = index
                else:
                    if index - start_index > max_sum:
                        max_sum = index - start_index
                    start_index = zero_index + 1
                    zero_index = index
        if index + 1 - start_index > max_sum:
            max_sum = index + 1 - start_index
        return max_sum


print(Solution().longest_sub_array([1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]))
print(Solution().longest_sub_array([1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]))
print(Solution().longest_sub_array([1, 1, 1, 1, 0]))

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        degree = 0
        sub_array_length = 0
        for index in range(len(nums)):
            current_degree = 1
            current_sub_array_length = 1
            frequency = {nums[index]: 1}
            for sub_index in range(index + 1, len(nums)):
                num_frequency = frequency.get(nums[sub_index])
                if num_frequency is None:
                    num_frequency = 1
                    frequency[nums[sub_index]] = num_frequency
                else:
                    num_frequency += 1
                    frequency[nums[sub_index]] = num_frequency

                if (current_degree < num_frequency) \
                        or (current_degree == num_frequency and current_sub_array_length > (sub_index + 1) - index):
                    current_degree = num_frequency
                    current_sub_array_length = (sub_index + 1) - index

            if degree < current_degree:
                degree = current_degree
                sub_array_length = current_sub_array_length
            elif degree == current_degree and current_sub_array_length < sub_array_length:
                sub_array_length = current_sub_array_length
            else:
                break

        return sub_array_length


print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))
print(Solution().findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))

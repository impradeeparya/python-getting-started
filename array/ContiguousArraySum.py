class Solution:
    def __init__(self, input_array, target_sum):
        self.input_array = input_array
        self.target_sum = target_sum

    def set_start_index(self, start_index, end_index):
        current_start_index = end_index
        while start_index < end_index + 1:
            if self.input_array[start_index] != 0:
                current_start_index = start_index
                break
            start_index += 1
        return current_start_index

    def sum(self):
        start_index = None
        end_index = None

        current_start_index = None
        current_sum = 0
        for index in range(len(self.input_array)):
            if current_start_index is None and self.input_array[index] > 0:
                current_start_index = index
            current_sum += self.input_array[index]
            if current_sum == self.target_sum:
                if start_index is None or ((end_index - start_index) > (index - current_start_index)):
                    start_index = current_start_index
                    end_index = index
                current_start_index = self.set_start_index(current_start_index + 1, index)
            elif current_sum > self.target_sum:
                current_sum -= self.input_array[current_start_index]
                current_start_index = self.set_start_index(current_start_index + 1, index)
                if current_sum == self.target_sum and (
                        start_index is None or ((end_index - start_index) > (index - current_start_index))):
                    start_index = current_start_index
                    end_index = index
                    current_start_index = self.set_start_index(current_start_index + 1, index)

        return end_index - start_index + 1


print(Solution([2, 10, 3, 7, 0, 0, 0, 2, 1], 10).sum())
print(Solution([2, 0, 3, 7, 0, 0, 0, 2, 1], 10).sum())
print(Solution([2, 3, 7, 0, 0, 0, 2, 1], 10).sum())

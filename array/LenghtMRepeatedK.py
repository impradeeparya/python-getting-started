# Given an array of positive integers arr,  find a pattern of length m that is repeated k or more times.
#
# A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times
# consecutively without overlapping. A pattern is defined by its length and the number of repetitions.
#
# Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.
from typing import List


class Solution:
    def is_same(self, arr, sub_arr):
        is_same = True
        for index in range(len(arr)):
            if arr[index] != sub_arr[index]:
                is_same = False
                break

        return is_same

    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        contain_pattern = False

        for index in range(len(arr)):
            end_index = index + m - 1

            sub_index = end_index + 1
            count = 0
            while (sub_index + m - 1) < len(arr):
                if self.is_same(arr[index:end_index + 1], arr[sub_index:sub_index + m]):
                    count = count + 1
                else:
                    break

                if count == k - 1:
                    contain_pattern = True
                    break
                sub_index = sub_index + m

            if contain_pattern:
                break

        return contain_pattern


print(Solution().containsPattern(arr=[1, 2, 4, 4, 4, 4], m=1, k=3))
print(Solution().containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
print(Solution().containsPattern(arr=[1, 2, 3, 1, 2], m=2, k=2))
print(Solution().containsPattern(arr=[2, 2, 2, 2], m=2, k=3))
print(Solution().containsPattern(arr=[2, 2], m=1, k=2))
print(Solution().containsPattern(arr=[2, 2, 1, 2, 2, 1, 1, 1, 2, 1], m=2, k=2))

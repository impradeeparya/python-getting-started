# Given an integer array nums and a positive integer k,return the most competitive subsequence of nums of size k.
#
# An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.
#
# We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first
# position where a and b differ,subsequence a has a number less than the corresponding number in b. For example,[1,
# 3,4] is more competitive than [1,3,5] because the first position they differ is at the final number,and 4 is less
# than 5.
from typing import List


class Solution:

    # def get_competitive_pair(self,pair1,pair2,k):
    #
    #     for index in range(k):
    #         if pair1[index] > pair2[index]:
    #             return pair2
    #
    #         if pair1[index] < pair2[index]:
    #             return pair1
    #
    #     return pair2
    #
    # def competitive_pair(self,nums,start_index,end_index,pair,competitive_pair,k):
    #     if len(pair) == k:
    #         if competitive_pair is None:
    #             return pair
    #         return self.get_competitive_pair(pair,competitive_pair,k)
    #
    #     for current_index in range(start_index,end_index):
    #         current_pair = pair.copy()
    #         current_pair.append(nums[current_index])
    #         competitive_pair = self.competitive_pair(nums,current_index + 1,end_index,current_pair,competitive_pair,
    #                                                  k)
    #
    #     return competitive_pair
    #
    # def mostCompetitive(self,nums: List[int],k: int) -> List[int]:
    #     n = len(nums)
    #     min_element = None
    #     end_index = n - k
    #     min_index = None
    #     for index,element in enumerate(nums):
    #         if index <= end_index:
    #             if (min_element is None) or (min_element > element):
    #                 min_element = element
    #                 min_index = index
    #         else:
    #             break
    #     print(min_element)
    #
    #     return self.competitive_pair(nums,min_index + 1,n,[nums[min_index]],None,k)

    def populate_min(self, nums, start_index, end_index, pair):
        index = start_index
        min_element = nums[index]
        sub_index = index + 1
        while sub_index < end_index:
            if nums[sub_index] < min_element:
                min_element = nums[sub_index]
                index = sub_index
            sub_index += 1
        pair.append(min_element)
        return index

    def competitive_pair(self, nums, start_index, end_index, pair, k, length, m):

        while start_index < end_index:
            if length == m:
                break
            elements_to_include = start_index + (end_index - start_index - k) + 1
            if elements_to_include >= end_index:
                elements_to_include = end_index
            start_index = self.populate_min(nums, start_index, elements_to_include, pair)
            start_index += 1
            k -= 1
            length += 1

        return pair

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        min_element = None
        end_index = n - k
        min_index = None
        for index in range(n):
            if index <= end_index:
                element = nums[index]
                if (min_element is None) or (min_element > element):
                    min_element = element
                    min_index = index
            else:
                break

        return self.competitive_pair(nums, min_index + 1, n, [nums[min_index]], k - 1, 1, k)


print("output [2,6] ", Solution().mostCompetitive(nums=[3, 5, 2, 6], k=2))
print("output [2,3,3,4] ", Solution().mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4))
print("output [8,80,2] ", Solution().mostCompetitive(nums=[71, 18, 52, 29, 55, 73, 24, 42, 66, 8, 80, 2], k=3))
print("output [10,23,61,62,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71] ", Solution().mostCompetitive(
    nums=[84, 10, 71, 23, 66, 61, 62, 64, 34, 41, 80, 25, 91, 43, 4, 75, 65, 13, 37, 41, 46, 90, 55, 8, 85, 61, 95, 71],
    k=24))
print("output [10,23,61,62,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71] ",
      Solution().mostCompetitive(
          nums=[84, 10, 71, 23, 66, 61, 62, 64, 34, 41, 80, 25, 91, 43, 4, 75, 65, 13, 37, 41, 46, 90, 55, 8, 85, 61,
                95, 71],
          k=24))
print("output [2,3,3,4] ", Solution().mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4))
print("output [0] ", Solution().mostCompetitive(
    [74, 80, 88, 14, 97, 53, 51, 29, 83, 91, 18, 9, 56, 86, 74, 86, 21, 18, 91, 70, 100, 25, 67, 16, 37, 35, 92, 74, 40,
     58, 2, 94, 47, 55, 36, 18, 41, 31, 32, 59, 77, 64, 41, 37, 59, 16, 0, 25, 88, 35, 76, 17, 70, 73, 35, 15, 46, 72,
     66, 44, 83, 74, 61, 63, 78, 14, 70, 96, 65, 47, 64, 35, 29, 19, 6, 95, 21, 49, 40, 52, 70, 91, 61, 21, 16, 73, 83,
     35, 30, 33, 49, 2, 59, 8, 6, 7, 37, 91, 51, 43, 53, 67, 90, 25, 55, 46, 56, 79, 99, 70, 69, 48, 83, 23, 84, 36, 52,
     36, 93, 40, 60, 99, 83],
    1))

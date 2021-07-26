# You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following
# algorithm on arr: # # Starting from left to right, remove the first number and every other number afterward until
# you reach the end of the list. # Repeat the previous step again, but this time from right to left, remove the
# rightmost number and every other number from the remaining numbers. # Keep repeating the steps again, alternating
# left to right and right to left, until a single number remains. # Given the integer n, return the last number that
# remains in arr.


class Solution:
    # def lastRemaining(self, n: int) -> int:
    #     elements = [element for element in range(1, n + 1)]
    #     # print(elements)
    #
    #     is_left = True
    #     last_element = None
    #     while elements:
    #
    #         del_indexes = []
    #         start_index = 0
    #         end_index = len(elements) - 1
    #         if is_left:
    #             while start_index <= end_index:
    #                 del_indexes.append(start_index)
    #                 start_index = start_index + 2
    #         else:
    #             while end_index >= start_index:
    #                 del_indexes.insert(0, end_index)
    #                 end_index = end_index - 2
    #
    #         del_element_index = 0
    #         for index in del_indexes:
    #             # print(index)
    #             index = index - del_element_index
    #             last_element = elements[index]
    #             del elements[index]
    #             del_element_index = del_element_index + 1
    #         print("deleted ", del_indexes)
    #
    #         is_left = not is_left
    #     return last_element

    # def lastRemaining(self, n: int) -> int:
    #     elements = [element for element in range(1, n + 1)]
    #     # print(elements)
    #
    #     is_left = True
    #     last_element = None
    #     while elements:
    #
    #         start_index = 0
    #         end_index = len(elements) - 1
    #         if is_left:
    #             while start_index < len(elements):
    #                 last_element = elements[start_index]
    #                 del elements[start_index]
    #                 start_index = start_index + 1
    #         else:
    #             while end_index >= 0:
    #                 last_element = elements[end_index]
    #                 del elements[end_index]
    #                 end_index = end_index - 2
    #
    #         is_left = not is_left
    #     return last_element

    # def lastRemaining(self, n: int) -> int:
    #     elements = [element for element in range(1, n + 1)]
    #     # print(elements)
    #
    #     is_left = True
    #     last_element = elements[0]
    #     while elements:
    #
    #         start_index = 0
    #         end_index = len(elements) - 1
    #         # print(elements)
    #         # print(start_index, end_index)
    #         temp = []
    #         if is_left:
    #             start_index = start_index + 1
    #             while start_index <= end_index:
    #                 last_element = elements[start_index]
    #                 temp.append(last_element)
    #                 start_index = start_index + 2
    #         else:
    #             end_index = end_index - 1
    #             while end_index >= 0:
    #                 last_element = elements[end_index]
    #                 temp.insert(0, last_element)
    #                 end_index = end_index - 2
    #
    #         is_left = not is_left
    #         elements = temp
    #
    #     return last_element

    def lastRemaining(self, n: int) -> int:
        element_left = 1
        round = 1
        is_left = True
        while n > 1:

            if is_left or (n % 2 == 1):
                element_left += round

            n = int(n / 2)
            round *= 2
            is_left = not is_left

        return element_left


print("output 6 ", Solution().lastRemaining(n=9))
print("output 2 ", Solution().lastRemaining(n=5))
print("output 1 ", Solution().lastRemaining(n=1))
print("output 349526 ", Solution().lastRemaining(n=1000000))
print("output 4 ", Solution().lastRemaining(n=7))

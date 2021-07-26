# You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1,
# 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*',
# '/'] and the parentheses '(' and ')' to get the value 24.
#
# You are restricted with the following rules:
#
# The division operator '/' represents real division, not integer division.
# For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
# Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
# For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
# You cannot concatenate numbers together
# For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
# Return true if you can get such expression that evaluates to 24, and false otherwise.
from typing import List


class Solution:

    # def is_24_point2(self, sum1, sum2):
    #     if sum1 < 24:
    #         return (sum1 + sum2 == 24) or (sum1 * sum2 == 24)
    #     else:
    #         return (sum1 - sum2 == 24) or (sum1 / sum2 == 24)
    #
    # def is_24_point1(self, sum1, v3, v4):
    #     add_value = self.is_24_point2(sum1, v3 + v4)
    #     sub_value = self.is_24_point2(sum1, v3 - v4)
    #     multiply_value = self.is_24_point2(sum1, v3 * v4)
    #     divide_value = self.is_24_point2(sum1, v3 / v4)
    #
    #     return add_value or sub_value or multiply_value or divide_value
    #
    # def is_24_point(self, v1, v2, v3, v4):
    #     add_value = self.is_24_point1(v1 + v2, v3, v4)
    #     sub_value = self.is_24_point1(v1 - v2, v3, v4)
    #     multiply_value = self.is_24_point1(v1 * v2, v3, v4)
    #     divide_value = self.is_24_point1(v1 / v2, v3, v4)
    #
    #     return add_value or sub_value or multiply_value or divide_value

    def perform_operations(self, x, y):
        operation_list = [x * y, x + y, x - y, y - x]
        if x:
            operation_list.append(y / x)
        if y:
            operation_list.append(x / y)
        return operation_list

    def judgePoint24(self, cards: List[int]) -> bool:

        if len(cards) == 1:
            if abs(cards[0] - 24) < 0.00001:
                return True
            else:
                return False

        for index in range(len(cards)):
            for sub_index in range(index + 1, len(cards)):
                x = cards[index]
                y = cards[sub_index]

                elements = self.perform_operations(x, y)
                new_cards = [cards[z] for z in range(len(cards)) if z not in (index, sub_index)]

                for element in elements:
                    new_cards.insert(0, element)
                    has_24 = self.judgePoint24(new_cards)
                    new_cards.pop(0)
                    if has_24:
                        return True
        return False


print(Solution().judgePoint24([4, 1, 8, 7]))
print(Solution().judgePoint24([1, 2, 1, 2]))
print(Solution().judgePoint24([1, 3, 4, 6]))
print(Solution().judgePoint24([3, 3, 8, 8]))

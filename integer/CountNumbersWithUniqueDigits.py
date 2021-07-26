# Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.


class Solution:
    # def is_unique(self, number):
    #
    #     if number / 10 == 0:
    #         return True
    #
    #     frequency = {}
    #     unique_number = number
    #     while unique_number > 0:
    #         modulo = unique_number % 10
    #         if frequency.get(modulo, None) is not None:
    #             return False
    #         frequency[modulo] = True
    #         unique_number = int(unique_number / 10)
    #     return True
    #
    # def countNumbersWithUniqueDigits(self, n: int) -> int:
    #     unique_count = 0
    #     for number in range(0, 10 ** n):
    #         if self.is_unique(number):
    #             unique_count = unique_count + 1
    #
    #     return unique_count

    # def unique_count(self, unique_number, visited, digit):
    #
    #     if len(unique_number) == digit:
    #         # print(unique_number)
    #         return 1
    #
    #     unique_count = 0
    #     for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    #         if visited & (1 << number) == 0:
    #             visited = visited | (1 << number)
    #             unique_count = unique_count + self.unique_count(unique_number + str(number), visited, digit)
    #             visited = visited & ~(1 << number)
    #
    #     return unique_count
    #
    # def countNumbersWithUniqueDigits(self, n: int) -> int:
    #     unique_count = 1
    #     for digit in range(1, n + 1):
    #         visited = 0
    #         for number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    #             visited = visited | (1 << number)
    #             unique_count = unique_count + self.unique_count(str(number), visited, digit)
    #             visited = 0
    #
    #     return unique_count

    def unique_count(self, unique_number, visited, digit, max_digits):

        if len(unique_number) > 1 and unique_number[0] == '0':
            return 0

        if len(unique_number) == max_digits:
            return 1

        unique_count = 0

        if digit > 0:
            unique_count = unique_count + 1

        for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if digit == 0 or (digit > 0 and unique_number[0] != '0'):
                if visited & (1 << number) == 0:
                    visited = visited | (1 << number)
                    unique_count = unique_count + self.unique_count(unique_number + str(number), visited, digit + 1,
                                                                    max_digits)
                    visited = visited & ~(1 << number)

        return unique_count

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return self.unique_count('', 0, 0, n)


print(Solution().countNumbersWithUniqueDigits(2))
print(Solution().countNumbersWithUniqueDigits(0))
print(Solution().countNumbersWithUniqueDigits(3))

# print(Solution().is_unique(990))
# print(Solution().unique_count('9', 1 << 9, 3))

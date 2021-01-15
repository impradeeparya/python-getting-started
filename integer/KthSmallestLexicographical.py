class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # numbers = []
        # for number in range(1, n + 1):
        #     numbers.append(str(number))
        # numbers.sort()
        # return numbers[k - 1]
        number = 1
        digit_number = 0
        pointer = number
        while number <= 9:
            is_found = False
            power = 1
            pointer = number
            digit_number += 1
            while pointer <= n:
                if digit_number == k:
                    is_found = True
                    break
                pointer = number * (10 ** power)
                digit_number += 1
                power += 1
            if is_found:
                break
            pointer = int(pointer / 10)
            digit_number -= 1

            while pointer > 0:
                pointer += 1
                digit_number += 1
                if pointer > n:
                    pointer = int(pointer / 10)
                    digit_number -= 1
                else:
                    p_digit = int(str(pointer)[0])
                    n_digit = int(str(number)[0])
                    if p_digit != n_digit:
                        digit_number -= 1
                        break
                if digit_number == k:
                    is_found = True
                    break

            if is_found:
                break
            number += 1
        return pointer


# print(Solution().findKthNumber(13, 2))
# print(Solution().findKthNumber(100, 10))
# print(Solution().findKthNumber(10, 3))
# print(Solution().findKthNumber(100, 90))
# print(Solution().findKthNumber(2, 2))
# print(Solution().findKthNumber(10000, 10000))
print(Solution().findKthNumber(1000, 1000))

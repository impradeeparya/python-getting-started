class Solution(object):
    def reverse(self, x):
        result = 0
        is_negative = True if x < 0 else False
        x = x * -1 if is_negative else x
        while x > 0:
            digit = x % 10
            result = result * 10 + digit
            x = int(x / 10)
        result = result * -1 if is_negative else result

        return result if -2 ** 31 <= result <= 2 ** 31 - 1 else 0


reverse_number = Solution().reverse(1534236469)
print(reverse_number)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        input_number = x
        reverse_number = 0
        while input_number > 0:
            last_digit = int(input_number % 10)
            reverse_number = reverse_number * 10 + last_digit
            input_number = int(input_number / 10)

        return True if x == reverse_number else False


is_palindrome = Solution().isPalindrome(121)
print(is_palindrome)

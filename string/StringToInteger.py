class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_start_index = 0
        for index, value in enumerate(s):
            if value != ' ':
                char_start_index = index
                break

        result = 0

        is_negative_integer = None

        if char_start_index >= len(s):
            return result
        elif s[char_start_index] == '-':
            is_negative_integer = True
            char_start_index += 1
        elif s[char_start_index] == '+':
            is_negative_integer = False
            char_start_index += 1
        elif 48 > ord(s[char_start_index]) > 57:
            return result

        for index in range(char_start_index, len(s)):
            if 48 <= ord(s[index]) <= 57:
                result = result * 10 + int(s[index])
            else:
                break

        signed_result = result * -1 if is_negative_integer else result

        if is_negative_integer:
            if signed_result <= -2 ** 31:
                signed_result = -2 ** 31 + 1
        else:
            if signed_result >= 2 ** 31:
                signed_result = 2 ** 31 - 1

        return signed_result


int_value = Solution().myAtoi("21474836460")
print(int_value)

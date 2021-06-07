class Solution(object):
    # def originalDigits(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     digits = [
    #         "zero",
    #         "one",
    #         "two",
    #         "three",
    #         "four",
    #         "five",
    #         "six",
    #         "seven",
    #         "eight",
    #         "nine"
    #     ]
    #     s_char_frequency = {}
    #     for index in range(len(s)):
    #         s_char = s[index]
    #         s_char_frequency[s_char] = s_char_frequency[s_char] + 1 if s_char_frequency.get(s_char,
    #                                                                                         None) is not None else 1
    #
    #     numeric_values = []
    #     for digit in range(len(digits)):
    #         is_word_found = True
    #         min_frequency = -1
    #         key = digits[digit]
    #         for index in range(len(key)):
    #             frequency = s_char_frequency.get(key[index], None)
    #             if frequency is None or frequency == 0:
    #                 is_word_found = False
    #                 break
    #             else:
    #                 min_frequency = frequency if min_frequency == -1 else min(min_frequency, frequency)
    #
    #         if is_word_found:
    #             for index in range(len(key)):
    #                 s_char_frequency[key[index]] = s_char_frequency[key[index]] - min_frequency
    #             for index in range(min_frequency):
    #                 numeric_values.append(str(digit))
    #
    #     numeric_values.sort()
    #     return "".join(numeric_values)

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0 for index in range(26)]
        for index in range(len(s)):
            char_value = s[index]
            if char_value == 'z':
                count[0] = count[0] + 1
            elif char_value == 'x':
                count[6] = count[6] + 1
            elif char_value == 'w':
                count[2] = count[2] + 1
            elif char_value == 'g':
                count[8] = count[8] + 1
            elif char_value == 'u':
                count[4] = count[4] + 1
            elif char_value == 's':
                count[7] = count[7] + 1
            elif char_value == 'f':
                count[5] = count[5] + 1
            elif char_value == 'h':
                count[3] = count[3] + 1
            elif char_value == 'i':
                count[9] = count[9] + 1
            elif char_value == 'o':
                count[1] = count[1] + 1

        count[7] -= count[6]
        count[5] -= count[4]
        count[3] -= count[8]
        count[9] = count[9] - count[8] - count[5] - count[6]
        count[1] = count[1] - count[0] - count[2] - count[4]

        output = ""
        for index in range(11):
            for frequency in range(count[index]):
                output += str(index)
        return output


print(Solution().originalDigits("owoztneoer"))
print(Solution().originalDigits("zerozero"))
print(Solution().originalDigits("zeroonetwothreefourfivesixseveneightnine"))

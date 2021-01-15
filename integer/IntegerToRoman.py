class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        number = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 40: "XL",
                  50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        roman_number = ""
        while num > 0:

            if number.get(num) is not None:
                roman_number += number.get(num)
                break
            elif 10 < num < 40:
                constant_number = 10
            elif 40 < num < 50:
                constant_number = 40
            elif 50 < num < 90:
                constant_number = 50
            elif 90 < num < 100:
                constant_number = 90
            elif 100 < num < 400:
                constant_number = 100
            elif 400 < num < 500:
                constant_number = 400
            elif 500 < num < 900:
                constant_number = 500
            elif 900 < num < 1000:
                constant_number = 900
            else:
                constant_number = 1000

            remainder = num % constant_number
            quotient = int(num / constant_number)
            roman_number += (number.get(constant_number) * quotient)
            num = remainder

        return roman_number


roman = Solution().intToRoman(1994)
print(roman)

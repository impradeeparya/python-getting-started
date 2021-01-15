class Solution(object):
    def processCombinations(self, digits_letters, letter_combination, index, digits):
        combinations = []
        if len(digits) - 1 == index:
            digit = digits[index]
            letters = digits_letters[digit]
            current_index = 0
            for letter in letters:
                combinations.insert(current_index, letter_combination + letter)
                current_index += 1
        elif index < len(digits):
            digit = digits[index]
            letters = digits_letters[digit]
            for letter in letters:
                combinations.extend(
                    self.processCombinations(digits_letters, letter_combination + letter, index + 1, digits))
        else:
            combinations.insert(0, letter_combination)

        return combinations

    def letterCombinations(self, digits):
        combinations = []
        digits_letters = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                          '6': ['m', 'n', 'o'],
                          '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if digits:
            index = 0
            digit = digits[index]
            letters = digits_letters[digit]
            for letter in letters:
                combinations.extend(self.processCombinations(digits_letters, letter, index + 1, digits))

        return combinations


print(Solution().letterCombinations(""))

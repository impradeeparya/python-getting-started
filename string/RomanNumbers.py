number = {"I": 1, "V": 5, "X": 10, "i": 1, "v": 5, "x": 10, "L": 50, "l": 50, "C": 100, "c": 100, "D": 500, "d": 500,
          "M": 1000, "m": 1000}


def get_number(roman_number_chars):
    last_index = len(roman_number_chars) - 1
    total_sum = number.get(roman_number_chars[last_index]) if number.get(
        roman_number_chars[last_index]) is not None else 0
    for index in range(last_index - 1, -1, -1):
        current_char_value = number.get(roman_number_chars[index]) if number.get(
            roman_number_chars[index]) is not None else 0
        last_char_value = number.get(roman_number_chars[index + 1]) if number.get(
            roman_number_chars[index + 1]) is not None else 0

        if current_char_value < last_char_value:
            total_sum -= current_char_value
        else:
            total_sum += current_char_value

    return total_sum


def roman_number():
    test_cases = int(input())
    for test_case in range(test_cases):
        input_roman_number = input()
        roman_number_chars = list(input_roman_number)
        print(get_number(roman_number_chars))


roman_number()

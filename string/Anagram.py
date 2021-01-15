def check_anagram():
    test_cases = int(input())
    for index in range(test_cases):
        input_str = input()

        input_split = input_str.split(" ")
        is_anagram = validate(input_split[0], input_split[1])
        print("YES" if is_anagram else "NO")


def validate(first_str, second_str):
    is_anagram = True
    if len(first_str) != len(second_str):
        is_anagram = False
    else:
        first_str_chars = list(first_str)
        second_str_chars = list(second_str)

        second_str_chars_frequency = {}

        for index in range(len(second_str_chars)):
            count = 0
            str_char = second_str_chars[index]
            if str_char in second_str_chars_frequency:
                count = second_str_chars_frequency[str_char]

            count += 1
            second_str_chars_frequency[str_char] = count

        for index in range(len(first_str_chars)):
            str_char = first_str_chars[index]
            if str_char in second_str_chars_frequency:
                count = second_str_chars_frequency[str_char]
                if count > 0:
                    count -= 1
                    second_str_chars_frequency[str_char] = count
                else:
                    is_anagram = False
                    break
            else:
                is_anagram = False

    return is_anagram


check_anagram()

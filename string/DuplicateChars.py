def remove_duplicate_chars(input_str):
    input_chars = list(input_str)
    counter = 0
    index = 0
    while index < len(input_chars):
        char_ascii = ord(input_chars[index])

        if counter & (1 << char_ascii) == 0:
            counter = counter | (1 << char_ascii)
        else:
            input_chars[index] = ""
        index += 1

    return "".join(input_chars)


def remove_duplicates():
    test_cases = int(input())
    for test_case in range(test_cases):
        input_str = input()
        print(remove_duplicate_chars(input_str))


remove_duplicates()

def get_count(input_chars, start_index, end_index):
    count = 0
    if start_index < end_index:
        if input_chars[start_index] == input_chars[end_index]:
            count = get_count(input_chars, start_index + 1, end_index - 1)
        else:
            count = 1 + min(get_count(input_chars, start_index + 1, end_index),
                            get_count(input_chars, start_index, end_index - 1))

    return count


def create_palindrome():
    test_cases = int(input())
    for test_case in range(test_cases):
        input_str = input()
        print(get_count(list(input_str), 0, len(input_str) - 1))
        # print(get_count(list(input_str)))


create_palindrome()

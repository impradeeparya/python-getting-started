def check_anticlockwise(first_chars, second_chars, rotation):
    is_same = True

    i = 0
    for index in range(rotation, len(first_chars) - rotation):
        if second_chars[i] != first_chars[index]:
            is_same = False
            break
        i += 1

    if is_same:
        i = 0
        for index in range(len(first_chars) - rotation, len(first_chars)):
            if first_chars[i] != second_chars[index]:
                is_same = False
                break
            i += 1

    return is_same


def check_clockwise(first_chars, second_chars, rotation):
    is_same = True
    i = 0
    for index in range(rotation, len(first_chars)):
        if first_chars[i] != second_chars[index]:
            is_same = False
            break
        i += 1

    if is_same:
        i = len(first_chars) - rotation
        for index in range(rotation):
            if first_chars[i] != second_chars[index]:
                is_same = False
                break
            i += 1

    return is_same


def validate_strings(first_str, second_str, rotation):
    first_chars = list(first_str)
    second_chars = list(second_str)

    is_same = check_anticlockwise(first_chars, second_chars, rotation)

    if not is_same:
        is_same = check_clockwise(first_chars, second_chars, rotation)

    return is_same


def rotated_string():
    test_cases = int(input())
    for test_case in range(test_cases):
        first_str = input()
        second_str = input()
        is_valid = validate_strings(first_str, second_str, 2) if len(first_str) == len(second_str) else False

        print(1 if is_valid else 0)


rotated_string()

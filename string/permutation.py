output = []
counter = 0


def swap(input_chars, index, swapped_index):
    temp = input_chars[index]
    input_chars[index] = input_chars[swapped_index]
    input_chars[swapped_index] = temp


def print_permutation(input_chars, start_index):
    if start_index == len(input_chars) - 1:
        global counter
        output.insert(counter, "".join(input_chars))
        counter += 1
    else:
        print_permutation(input_chars, start_index + 1)
        for index in range(start_index, len(input_chars) - 1):
            swap(input_chars, start_index, index + 1)
            print_permutation(input_chars, start_index + 1)
            swap(input_chars, start_index, index + 1)


def permutation():
    number_test_cases = int(input())

    for test in range(number_test_cases):
        input_str = input()
        input_chars = list(input_str)
        print_permutation(input_chars, 0)
        global output
        output.sort(reverse=False)
        print(" ".join(output))
        output = []
        global counter
        counter = 0


permutation()

def reverse_word(start_index, end_index, word):
    while start_index < end_index:
        temp = word[start_index]
        word[start_index] = word[end_index]
        word[end_index] = temp
        start_index += 1
        end_index -= 1


def reverse_words(line, delimiter):
    line_chars = list(line)

    start_index = 0
    for index in range(len(line_chars)):

        if line_chars[index] == delimiter:
            end_index = index - 1
            reverse_word(start_index, end_index, line_chars)
            start_index = index + 1

        if index == len(line_chars) - 1:
            end_index = index
            reverse_word(start_index, end_index, line_chars)
            start_index = index + 1

    return "".join(line_chars)


def reverse_line(line):
    start_index = 0
    end_index = len(line) - 1
    line_chars = list(line)
    while start_index < end_index:
        temp = line_chars[start_index]
        line_chars[start_index] = line_chars[end_index]
        line_chars[end_index] = temp
        start_index += 1
        end_index -= 1
    return "".join(line_chars)


def string_reverse():
    input_lines = int(input())
    lines = []
    for index in range(input_lines):
        line = input()
        lines.insert(index, line)

    for index in range(input_lines):
        reversed_word = reverse_words(lines[index], '.')
        reversed_line = reverse_line(reversed_word)
        print(reversed_line)


string_reverse()

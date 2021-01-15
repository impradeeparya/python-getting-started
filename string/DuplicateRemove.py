def remove(input_chars):
    prev_index = 0
    index = 1
    while index < len(input_chars):

        if input_chars[prev_index] == input_chars[index]:
            input_chars[prev_index] = input_chars[index] = 0
            if prev_index == 0:
                prev_index = index + 1
                index += 1
            else:
                prev_index -= 1
        else:
            prev_index = index
        index += 1


def remove_duplicate():
    number_of_test_cases = int(input())
    for test_case in range(number_of_test_cases):
        input_str = input()
        input_chars = list(input_str)
        remove(input_chars)
        for index in range(len(input_chars)):
            char = input_chars[index]
            if char != 0:
                print(char, end="")
        print()


remove_duplicate()

# def removeUtil(string, last_removed):
#     # If length of string is 1 or 0
#     if len(string) == 0 or len(string) == 1:
#         return string
#
#         # Remove leftmost same characters and recur for remaining
#     # string
#     if string[0] == string[1]:
#         last_removed = ord(string[0])
#         while len(string) > 1 and string[0] == string[1]:
#             string = string[1:]
#         string = string[1:]
#
#         return removeUtil(string, last_removed)
#
#         # At this point, the first character is definiotely different
#     # from its adjacent. Ignore first character and recursively
#     # remove characters from remaining string
#     rem_str = removeUtil(string[1:], last_removed)
#
#     # Check if the first character of the rem_string matches
#     # with the first character of the original string
#     if len(rem_str) != 0 and rem_str[0] == string[0]:
#         last_removed = ord(string[0])
#         return (rem_str[1:])
#
#         # If remaining string becomes empty and last removed character
#     # is same as first character of original string. This is needed
#     # for a string like "acbbcddc"
#     if len(rem_str) == 0 and last_removed == ord(string[0]):
#         return rem_str
#
#         # If the two first characters of str and rem_str don't match,
#     # append first character of str before the first character of
#     # rem_str.
#     return ([string[0]] + rem_str)
#
#
# def remove(string):
#     last_removed = 0
#     return toString(removeUtil(toList(string), last_removed))
#
#
# # Utility functions
# def toList(string):
#     x = []
#     for i in string:
#         x.append(i)
#     return x
#
#
# def toString(x):
#     return ''.join(x)
#
#
# # Driver program
# string1 = "acaaabbbaacdddd"
# print(remove(string1))

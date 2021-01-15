class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_duplicate_indexes = {}
        for index in range(len(s)):
            s_char = s[index]
            indexes = char_duplicate_indexes.get(s_char)
            if indexes is None:
                char_duplicate_indexes[s_char] = [index]
            else:
                indexes.append(index)
                char_duplicate_indexes[s_char] = indexes

        print(char_duplicate_indexes)

        i = 0
        j = 0
        longest_length = 0
        for index in range(len(s)):
            s_char = s[index]
            duplicate_indexes = char_duplicate_indexes.get(s_char)
            if len(duplicate_indexes) == 1 and longest_length == 0:
                longest_length = 1
                i = index
                j = index
            else:
                if len(duplicate_indexes) == 1:
                    if duplicate_indexes[0] - j == 1 and duplicate_indexes[0] > j:
                        j = duplicate_indexes[0]
                        longest_length += 1

                else:
                    if duplicate_indexes[0] - j == 1 and duplicate_indexes[0] > j:
                        longest_length += duplicate_indexes[1] - duplicate_indexes[0]
                        j = duplicate_indexes[0]

                    for duplicate_index in range(1, len(duplicate_indexes)):
                        length = duplicate_indexes[duplicate_index] - duplicate_indexes[duplicate_index - 1]
                        if length > longest_length:
                            longest_length = length
                            i = duplicate_indexes[duplicate_index - 1]
                            j = duplicate_indexes[duplicate_index]

        print(i, j)
        return longest_length


NO_OF_CHARS = 256


def longestUniqueSubsttr(string):

    # Initialize the last index array as -1, -1 is used to store
    # last index of every character
    lastIndex = [-1] * NO_OF_CHARS

    n = len(string)
    res = 0   # Result
    i = 0

    for j in range(0, n):
        # Find the last index of str[j]
        # Update i (starting index of current window)
        # as maximum of current value of i and last
        # index plus 1
        i = max(i, lastIndex[ord(string[j])] + 1);

        # Update result if we get a larger window
        res =  max(res, j - i + 1)

        # Update last index of j.
        lastIndex[ord(string[j])] = j;

    return res


string = "abba"
print ("The input string is " + string)
length = longestUniqueSubsttr(string)
print ("The length of the longest non-repeating character" +
       " substring is " + str(length))

# substring_length = Solution().lengthOfLongestSubstring("abba")
# print(substring_length)

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer
# in any order.


class Solution(object):
    def get_frequency(self, s):
        p_frequency = {}
        for element in s:
            frequency = p_frequency.get(element, None)
            if frequency is None:
                frequency = 1
            else:
                frequency += 1
            p_frequency[element] = frequency

        return p_frequency

    def is_valid(self, start_index, end_index, s, p_frequency):
        for index in range(start_index, end_index):
            element = s[index]
            frequency = p_frequency.get(element, None)
            if frequency is None:
                return False
            else:
                frequency -= 1
                if frequency == 0:
                    del p_frequency[element]
                else:
                    p_frequency[element] = frequency

        return len(p_frequency) == 0

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        m = len(p)
        output = []
        p_frequency = self.get_frequency(p)
        for index in range(n - m + 1):
            if self.is_valid(index, index + m, s, p_frequency):
                output.append(index)

        return output


print("output [0,1,2] ", Solution().findAnagrams(s="abab", p="ab"))

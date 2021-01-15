class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""

        if not not strs:
            min_len = len(strs[0])
            for index in range(1, len(strs)):
                str_len = len(strs[index])
                if str_len < min_len:
                    min_len = str_len

            for index in range(min_len):
                char = strs[0][index]
                for str_index in range(1, len(strs)):
                    if strs[str_index][index] != char:
                        return prefix

                prefix += char
        return prefix


longest_prefix = Solution().longestCommonPrefix([])
print(longest_prefix)

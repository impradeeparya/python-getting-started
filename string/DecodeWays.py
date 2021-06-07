class Solution:

    def decoding_count(self, s, n):
        if n == 0 or n == 1:
            return 1
        count = 0
        if s[n-1] > '0':
            count = self.decoding_count(s, n - 1)
        if s[n - 2] == '1' or (s[n - 2] == '2' and s[n] < '7'):
            count += self.decoding_count(s, n - 2)

        return count

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 0) or \
                (len(s) == 1 and s[0] == '0'):
            return 0

        return self.decoding_count(s, len(s))


print(Solution().numDecodings("11106"))
